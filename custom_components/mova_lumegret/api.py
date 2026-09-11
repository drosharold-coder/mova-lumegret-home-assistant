"""Read-only MOVA LumeGret cloud client."""
from __future__ import annotations

import hashlib
import json
import random
import re
import time
from typing import Any

from aiohttp import ClientError, ClientSession

from .const import MODEL_A4000, MODEL_P1

BASE_URL = "https://eu.iot.mova-tech.com:13267"
LOGIN_PATH = "/dreame-auth/oauth/token"
DEVICE_LIST_PATH = "/dreame-user-iot/iotuserbind/device/listV2"

PASSWORD_SALT = "RAylYC%fmSKp7%Tq"
APP_AUTH = "Basic ZHJlYW1lX2FwcHYxOkFQXmR2QHpAU1FZVnhOODg="
DEFAULT_TENANT_ID = "000002"
USER_AGENT = "Dart/3.2 (dart:io)"
DREAME_META = "cv=i_829"
DREAME_RLC = "1a9bb36e6b22617cf465363ba7c232fb131899d593e8d1a1-1"


class MovaError(Exception):
    pass


class MovaAuthError(MovaError):
    pass


class MovaConnectionError(MovaError):
    pass


def _compact_json(data: Any) -> str:
    return json.dumps(data, separators=(",", ":"), ensure_ascii=False)


def _normalize_model(value: Any) -> str:
    return str(value or "").replace("\\", "")


def _shard_from_domain(domain: Any) -> str | None:
    match = re.match(r"^(\d+)\.", str(domain or ""))
    return match.group(1) if match else None


def _find_records(obj: Any) -> list[dict[str, Any]] | None:
    if isinstance(obj, dict):
        if isinstance(obj.get("records"), list):
            return [x for x in obj["records"] if isinstance(x, dict)]
        for value in obj.values():
            found = _find_records(value)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = _find_records(value)
            if found is not None:
                return found
    return None


def _signed16(value: Any) -> int | float | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return int(value)
    if not isinstance(value, (int, float)):
        return None
    if isinstance(value, float) and not value.is_integer():
        return value
    value = int(value)
    return value - 65536 if value >= 32768 else value


class MovaCloudApi:
    """Minimal read-only MOVAhome EU client."""

    def __init__(self, session: ClientSession, email: str, password: str) -> None:
        self._session = session
        self._email = email.strip()
        self._password = password
        self._access_token: str | None = None
        self._refresh_token: str | None = None
        self._tenant_id = DEFAULT_TENANT_ID
        self._devices: dict[str, dict[str, Any]] = {}

    def _login_headers(self) -> dict[str, str]:
        return {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Language": "nl-NL,nl;q=0.9,en;q=0.8",
            "User-Agent": USER_AGENT,
            "Authorization": APP_AUTH,
            "Tenant-Id": self._tenant_id,
            "Dreame-Auth": "bearer",
            "dreame-meta": DREAME_META,
            "dreame-rlc": DREAME_RLC,
        }

    def _cloud_headers(self) -> dict[str, str]:
        if not self._access_token:
            raise MovaAuthError("Geen access token")
        return {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Accept-Language": "nl-NL,nl;q=0.9,en;q=0.8",
            "User-Agent": USER_AGENT,
            "Authorization": APP_AUTH,
            "Tenant-Id": self._tenant_id,
            "Dreame-Auth": f"bearer {self._access_token}",
            "dreame-meta": DREAME_META,
            "dreame-rlc": DREAME_RLC,
        }

    async def async_login(self) -> None:
        password_hash = hashlib.md5(
            (self._password + PASSWORD_SALT).encode("utf-8")
        ).hexdigest()
        form = {
            "grant_type": "password",
            "scope": "all",
            "platform": "IOS",
            "type": "account",
            "username": self._email,
            "password": password_hash,
            "country": "NL",
            "lang": "nl",
        }
        try:
            async with self._session.post(
                BASE_URL + LOGIN_PATH,
                headers=self._login_headers(),
                data=form,
                timeout=15,
            ) as response:
                payload = await response.json(content_type=None)
        except (ClientError, TimeoutError, ValueError) as err:
            raise MovaConnectionError(f"Loginverbinding mislukt: {err}") from err

        if response.status == 401:
            raise MovaAuthError("MOVAhome login geweigerd")
        if response.status != 200 or not isinstance(payload, dict):
            raise MovaConnectionError(f"Login HTTP {response.status}")

        token = payload.get("access_token")
        if not token:
            raise MovaAuthError(
                str(payload.get("error_description") or payload.get("error") or "Geen token")
            )

        self._access_token = str(token)
        if payload.get("refresh_token"):
            self._refresh_token = str(payload["refresh_token"])
        self._tenant_id = str(payload.get("tenant_id") or DEFAULT_TENANT_ID)

    async def async_refresh(self) -> None:
        if not self._refresh_token:
            await self.async_login()
            return

        form = {
            "platform": "IOS",
            "scope": "all",
            "grant_type": "refresh_token",
            "refresh_token": self._refresh_token,
        }
        try:
            async with self._session.post(
                BASE_URL + LOGIN_PATH,
                headers=self._login_headers(),
                data=form,
                timeout=15,
            ) as response:
                payload = await response.json(content_type=None)
        except (ClientError, TimeoutError, ValueError):
            await self.async_login()
            return

        if response.status != 200 or not isinstance(payload, dict) or not payload.get("access_token"):
            await self.async_login()
            return

        self._access_token = str(payload["access_token"])
        if payload.get("refresh_token"):
            self._refresh_token = str(payload["refresh_token"])
        self._tenant_id = str(payload.get("tenant_id") or self._tenant_id)

    async def _post_json(
        self,
        path: str,
        payload: dict[str, Any],
        retry_auth: bool = True,
    ) -> dict[str, Any] | list[Any]:
        if not self._access_token:
            await self.async_login()

        try:
            async with self._session.post(
                BASE_URL + path,
                headers=self._cloud_headers(),
                data=_compact_json(payload),
                timeout=15,
            ) as response:
                if response.status == 401 and retry_auth:
                    await self.async_refresh()
                    return await self._post_json(path, payload, False)
                data = await response.json(content_type=None)
        except (ClientError, TimeoutError, ValueError) as err:
            raise MovaConnectionError(f"Cloudverzoek mislukt: {err}") from err

        if response.status == 401:
            raise MovaAuthError("MOVA token geweigerd")
        if response.status != 200:
            raise MovaConnectionError(f"Cloud HTTP {response.status}")
        if not isinstance(data, (dict, list)):
            raise MovaConnectionError("Onverwachte MOVA response")

        if isinstance(data, dict) and data.get("code") not in (None, 0, "0"):
            raise MovaConnectionError(
                f"MOVA code {data.get('code')}: {data.get('msg') or data.get('message') or ''}"
            )
        return data

    async def async_discover_devices(self) -> dict[str, dict[str, Any]]:
        data = await self._post_json(
            DEVICE_LIST_PATH,
            {
                "sharedStatus": 1,
                "current": 1,
                "size": 100,
                "lang": "nl",
                "timestamp": int(time.time() * 1000),
            },
        )
        records = _find_records(data)
        if records is None:
            raise MovaConnectionError("Geen apparatenlijst gevonden")

        found: dict[str, dict[str, Any]] = {}
        for device in records:
            model = _normalize_model(device.get("model"))
            if model not in (MODEL_A4000, MODEL_P1):
                continue
            did = device.get("did")
            shard = _shard_from_domain(device.get("bindDomain"))
            if did is None or shard is None:
                continue
            found[model] = {
                "did": str(did),
                "shard": shard,
                "model": model,
            }

        self._devices = found
        return found

    async def async_get_properties(
        self,
        device: dict[str, Any],
        pairs: list[tuple[int, int]],
    ) -> dict[str, Any]:
        request_id = random.randint(100000, 999999)
        payload = {
            "did": device["did"],
            "id": request_id,
            "data": {
                "did": device["did"],
                "id": request_id,
                "method": "get_properties",
                "params": [
                    {
                        "did": f"{siid}.{piid}",
                        "siid": siid,
                        "piid": piid,
                    }
                    for siid, piid in pairs
                ],
                "from": "ios",
            },
        }

        data = await self._post_json(
            f"/dreame-iot-com-{device['shard']}/device/sendCommand",
            payload,
        )
        result: dict[str, Any] = {}

        def walk(obj: Any) -> None:
            if isinstance(obj, dict):
                if (
                    "siid" in obj
                    and "piid" in obj
                    and "value" in obj
                    and obj.get("code") in (None, 0, "0")
                ):
                    try:
                        result[f"{int(obj['siid'])}.{int(obj['piid'])}"] = obj["value"]
                    except (TypeError, ValueError):
                        pass
                for value in obj.values():
                    if isinstance(value, (dict, list)):
                        walk(value)
            elif isinstance(obj, list):
                for value in obj:
                    walk(value)

        walk(data)
        return result

    async def async_get_live_data(self) -> dict[str, Any]:
        if MODEL_A4000 not in self._devices or MODEL_P1 not in self._devices:
            await self.async_discover_devices()

        if MODEL_A4000 not in self._devices or MODEL_P1 not in self._devices:
            raise MovaConnectionError("A4000 en/of Smart Meter P1 niet gevonden")

        battery = await self.async_get_properties(
            self._devices[MODEL_A4000],
            [(2, 1), (3, 1), (5, 18), (5, 19), (7, 2)],
        )
        meter = await self.async_get_properties(
            self._devices[MODEL_P1],
            [(5, 8)],
        )

        status_code = battery.get("2.1")
        soc = battery.get("3.1")
        battery_power = _signed16(battery.get("5.19"))
        current_tenths = _signed16(battery.get("5.18"))
        internal_grid = _signed16(battery.get("7.2"))
        grid_kw = meter.get("5.8")

        if isinstance(soc, (int, float)) and not isinstance(soc, bool):
            soc = float(soc)
        else:
            soc = None

        if isinstance(status_code, (int, float)) and not isinstance(status_code, bool):
            status_code = int(status_code)
        else:
            status_code = None

        if isinstance(battery_power, (int, float)):
            battery_power = float(battery_power)
            charge_power = max(-battery_power, 0.0)
            discharge_power = max(battery_power, 0.0)
            direction = "Ontladen" if battery_power > 50 else "Laden" if battery_power < -50 else "Rust"
        else:
            battery_power = None
            charge_power = None
            discharge_power = None
            direction = None

        current = (
            round(float(current_tenths) / 10.0, 1)
            if isinstance(current_tenths, (int, float))
            else None
        )

        if isinstance(grid_kw, (int, float)) and not isinstance(grid_kw, bool):
            grid_power = round(float(grid_kw) * 1000.0, 1)
            import_power = max(grid_power, 0.0)
            export_power = max(-grid_power, 0.0)
        else:
            grid_power = None
            import_power = None
            export_power = None

        return {
            "battery_soc": soc,
            "battery_power": battery_power,
            "battery_charge_power": charge_power,
            "battery_discharge_power": discharge_power,
            "battery_current": current,
            "battery_direction": direction,
            "grid_power": grid_power,
            "grid_import_power": import_power,
            "grid_export_power": export_power,
            "operating_status_code": status_code,
            "internal_grid_power": internal_grid,
        }
