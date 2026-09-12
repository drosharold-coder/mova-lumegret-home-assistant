"""Unit tests for MOVA telemetry parsing without real hardware."""
from __future__ import annotations

import pytest

from custom_components.mova_lumegret.api import MovaCloudApi, _signed16
from custom_components.mova_lumegret.const import MODEL_A4000, MODEL_P1


class FakeMovaCloudApi(MovaCloudApi):
    """MOVA API test double backed by fixed property dictionaries."""

    def __init__(self, battery: dict, meter: dict) -> None:
        # The session is never used because async_get_properties is overridden.
        super().__init__(object(), "test@example.com", "not-a-real-password")
        self._battery = battery
        self._meter = meter
        self._devices = {
            MODEL_A4000: {"did": "battery", "shard": "1", "model": MODEL_A4000},
            MODEL_P1: {"did": "meter", "shard": "1", "model": MODEL_P1},
        }

    async def async_get_properties(self, device: dict, pairs: list[tuple[int, int]]) -> dict:
        del pairs
        if device["model"] == MODEL_A4000:
            return self._battery
        return self._meter


def test_signed16_conversion() -> None:
    assert _signed16(0) == 0
    assert _signed16(32767) == 32767
    assert _signed16(32768) == -32768
    assert _signed16(65535) == -1
    assert _signed16(12.5) == 12.5
    assert _signed16(None) is None


@pytest.mark.asyncio
async def test_charging_and_grid_import() -> None:
    api = FakeMovaCloudApi(
        battery={
            "2.1": 1,
            "3.1": 55,
            "5.18": 123,
            "5.19": 65536 - 800,
            "7.2": 250,
        },
        meter={"5.8": 1.25},
    )

    data = await api.async_get_live_data()

    assert data["battery_soc"] == 55.0
    assert data["battery_power"] == -800.0
    assert data["battery_charge_power"] == 800.0
    assert data["battery_discharge_power"] == 0.0
    assert data["battery_current"] == 12.3
    assert data["battery_direction"] == "Laden"
    assert data["grid_power"] == 1250.0
    assert data["grid_import_power"] == 1250.0
    assert data["grid_export_power"] == 0.0


@pytest.mark.asyncio
async def test_discharging_and_grid_export() -> None:
    api = FakeMovaCloudApi(
        battery={
            "2.1": 2,
            "3.1": 80,
            "5.18": 65536 - 45,
            "5.19": 950,
            "7.2": 65536 - 150,
        },
        meter={"5.8": -0.6},
    )

    data = await api.async_get_live_data()

    assert data["battery_power"] == 950.0
    assert data["battery_charge_power"] == 0.0
    assert data["battery_discharge_power"] == 950.0
    assert data["battery_current"] == -4.5
    assert data["battery_direction"] == "Ontladen"
    assert data["grid_power"] == -600.0
    assert data["grid_import_power"] == 0.0
    assert data["grid_export_power"] == 600.0
    assert data["internal_grid_power"] == -150


@pytest.mark.asyncio
async def test_idle_threshold() -> None:
    api = FakeMovaCloudApi(
        battery={"2.1": 0, "3.1": 40, "5.18": 0, "5.19": 50, "7.2": 0},
        meter={"5.8": 0},
    )

    data = await api.async_get_live_data()

    assert data["battery_direction"] == "Rust"
    assert data["battery_discharge_power"] == 50.0
    assert data["grid_import_power"] == 0.0
    assert data["grid_export_power"] == 0.0


@pytest.mark.asyncio
async def test_missing_values_remain_none() -> None:
    api = FakeMovaCloudApi(battery={}, meter={})

    data = await api.async_get_live_data()

    assert data["battery_soc"] is None
    assert data["battery_power"] is None
    assert data["battery_charge_power"] is None
    assert data["battery_discharge_power"] is None
    assert data["battery_current"] is None
    assert data["battery_direction"] is None
    assert data["grid_power"] is None
    assert data["grid_import_power"] is None
    assert data["grid_export_power"] is None
    assert data["operating_status_code"] is None
    assert data["internal_grid_power"] is None
