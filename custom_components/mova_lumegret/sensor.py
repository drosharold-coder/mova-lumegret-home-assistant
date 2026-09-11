"""Sensors for MOVA LumeGret Energy."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE, UnitOfElectricCurrent, UnitOfPower
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MODEL_A4000, MODEL_P1, STATUS_MAP
from .coordinator import MovaDataUpdateCoordinator


@dataclass(frozen=True, kw_only=True)
class MovaSensorDescription(SensorEntityDescription):
    data_key: str
    device_key: str
    value_fn: Callable[[dict[str, Any]], Any] | None = None


SENSORS = (
    MovaSensorDescription(
        key="battery_soc",
        name="Batterij SoC",
        data_key="battery_soc",
        device_key="battery",
        device_class=SensorDeviceClass.BATTERY,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:battery",
    ),
    MovaSensorDescription(
        key="battery_power",
        name="Batterijvermogen",
        data_key="battery_power",
        device_key="battery",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:battery-charging",
    ),
    MovaSensorDescription(
        key="battery_charge_power",
        name="Batterij laden",
        data_key="battery_charge_power",
        device_key="battery",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    MovaSensorDescription(
        key="battery_discharge_power",
        name="Batterij ontladen",
        data_key="battery_discharge_power",
        device_key="battery",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    MovaSensorDescription(
        key="battery_current",
        name="Batterijstroom",
        data_key="battery_current",
        device_key="battery",
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    MovaSensorDescription(
        key="battery_direction",
        name="Batterijrichting",
        data_key="battery_direction",
        device_key="battery",
        icon="mdi:swap-vertical",
    ),
    MovaSensorDescription(
        key="operating_status",
        name="Bedrijfsstatus",
        data_key="operating_status_code",
        device_key="battery",
        value_fn=lambda data: STATUS_MAP.get(
            data.get("operating_status_code"),
            f"Onbekend ({data.get('operating_status_code')})"
            if data.get("operating_status_code") is not None else None,
        ),
        icon="mdi:state-machine",
    ),
    MovaSensorDescription(
        key="grid_power",
        name="Netvermogen",
        data_key="grid_power",
        device_key="meter",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:transmission-tower",
    ),
    MovaSensorDescription(
        key="grid_import_power",
        name="Netafname",
        data_key="grid_import_power",
        device_key="meter",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    MovaSensorDescription(
        key="grid_export_power",
        name="Teruglevering",
        data_key="grid_export_power",
        device_key="meter",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    coordinator: MovaDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        MovaSensor(coordinator, entry, description)
        for description in SENSORS
    )


class MovaSensor(CoordinatorEntity[MovaDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: MovaDataUpdateCoordinator,
        entry: ConfigEntry,
        description: MovaSensorDescription,
    ) -> None:
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{entry.entry_id}_{description.key}"

        if description.device_key == "battery":
            self._attr_device_info = DeviceInfo(
                identifiers={(DOMAIN, f"{entry.entry_id}_{MODEL_A4000}")},
                manufacturer="MOVA",
                model="LumeGret A4000",
                name="MOVA LumeGret A4000",
            )
        else:
            self._attr_device_info = DeviceInfo(
                identifiers={(DOMAIN, f"{entry.entry_id}_{MODEL_P1}")},
                manufacturer="MOVA",
                model="Smart Meter P1",
                name="MOVA Smart Meter P1",
            )

    @property
    def native_value(self) -> Any:
        data = self.coordinator.data or {}
        description = self.entity_description
        if description.value_fn is not None:
            return description.value_fn(data)
        return data.get(description.data_key)

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        data = self.coordinator.data or {}
        if self.entity_description.key == "operating_status":
            return {"status_code": data.get("operating_status_code")}
        if self.entity_description.key == "grid_power":
            return {
                "a4000_internal_grid_power_w": data.get("internal_grid_power")
            }
        if self.entity_description.key == "battery_power":
            return {"sign": "positive=ontladen, negative=laden"}
        return None
