"""Coordinator for MOVA LumeGret Energy."""
from __future__ import annotations

import asyncio
from datetime import timedelta
import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import MovaAuthError, MovaCloudApi, MovaConnectionError
from .const import DEFAULT_SCAN_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)

_RETRY_DELAY_SECONDS = 2


class MovaDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Coordinate read-only MOVA cloud updates."""

    def __init__(self, hass: HomeAssistant, api: MovaCloudApi) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.api = api

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch the latest data and gracefully handle temporary failures."""
        try:
            return await self.api.async_get_live_data()
        except MovaAuthError as err:
            _LOGGER.debug("MOVA authentication expired; refreshing session")
            try:
                await self.api.async_refresh()
                return await self.api.async_get_live_data()
            except (MovaAuthError, MovaConnectionError) as retry_err:
                raise UpdateFailed(
                    f"MOVA authentication failed after retry: {retry_err}"
                ) from retry_err
            except Exception as retry_err:
                _LOGGER.exception("Unexpected MOVA authentication retry error")
                raise UpdateFailed(
                    "Unexpected error while renewing the MOVA session"
                ) from retry_err
        except MovaConnectionError as err:
            _LOGGER.debug(
                "Temporary MOVA connection error; retrying once in %s seconds: %s",
                _RETRY_DELAY_SECONDS,
                err,
            )
            await asyncio.sleep(_RETRY_DELAY_SECONDS)
            try:
                return await self.api.async_get_live_data()
            except (MovaAuthError, MovaConnectionError) as retry_err:
                raise UpdateFailed(
                    f"MOVA cloud unavailable after retry: {retry_err}"
                ) from retry_err
            except Exception as retry_err:
                _LOGGER.exception("Unexpected MOVA retry error")
                raise UpdateFailed(
                    "Unexpected error while retrying the MOVA cloud request"
                ) from retry_err
        except Exception as err:
            _LOGGER.exception("Unexpected MOVA coordinator error")
            raise UpdateFailed("Unexpected error while updating MOVA data") from err
