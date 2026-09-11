"""Coordinator for MOVA LumeGret Energy."""
from __future__ import annotations

from datetime import timedelta
from typing import Any
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import MovaAuthError, MovaCloudApi, MovaConnectionError
from .const import DEFAULT_SCAN_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)


class MovaDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    def __init__(self, hass: HomeAssistant, api: MovaCloudApi) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.api = api

    async def _async_update_data(self) -> dict[str, Any]:
        try:
            return await self.api.async_get_live_data()
        except MovaAuthError as err:
            try:
                await self.api.async_refresh()
                return await self.api.async_get_live_data()
            except Exception as retry_err:
                raise UpdateFailed(f"MOVA authenticatie mislukt: {retry_err}") from retry_err
        except MovaConnectionError as err:
            raise UpdateFailed(str(err)) from err
