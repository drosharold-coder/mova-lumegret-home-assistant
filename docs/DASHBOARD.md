# Dashboard examples

The integration exposes live MOVA battery and grid telemetry that can be used in normal Home Assistant dashboards. The exact entity IDs can differ depending on language/history, so always confirm the entity IDs in your own installation before copying YAML.

## Simple entities card

A simple dashboard card can include:

- battery SoC;
- battery power;
- charging power;
- discharging power;
- battery current;
- operating status;
- grid power;
- grid import;
- grid export.

Example structure:

```yaml
type: entities
title: MOVA Energy
entities:
  - entity: sensor.YOUR_A4000_SOC_ENTITY
    name: Battery SoC
  - entity: sensor.YOUR_A4000_POWER_ENTITY
    name: Battery power
  - entity: sensor.mova_lumegret_a4000_batterij_laden
    name: Charging
  - entity: sensor.mova_lumegret_a4000_batterij_ontladen
    name: Discharging
  - entity: sensor.YOUR_P1_GRID_POWER_ENTITY
    name: Grid power
```

Replace every placeholder with the actual entity ID shown in **Settings -> Devices & services -> Entities**.

## Home Assistant Energy Dashboard

The repository includes:

`optional/mova_energy_dashboard.yaml`

This optional package converts live charging/discharging power to cumulative energy (kWh) sensors that can be selected in the Home Assistant Energy Dashboard.

The package currently expects these source entity IDs:

```text
sensor.mova_lumegret_a4000_batterij_laden
sensor.mova_lumegret_a4000_batterij_ontladen
```

Check them before use. If your entity IDs differ, edit the package first.

A common package location is:

```text
/config/packages/mova_energy_dashboard.yaml
```

Your Home Assistant configuration must have packages enabled. After copying/updating the package:

1. Check Home Assistant configuration.
2. Restart Home Assistant.
3. Confirm the new cumulative kWh entities exist.
4. Open **Settings -> Dashboards -> Energy**.
5. Add the relevant battery charge/discharge energy sensors under battery storage.

## Power sign convention

- Battery power: positive = discharging, negative = charging.
- Grid power: positive = import, negative = export.

The dedicated charge/discharge and import/export sensors are often easier to use in dashboards than a signed combined value.
