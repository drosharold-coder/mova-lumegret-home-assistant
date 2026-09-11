# MOVA LumeGret Energy for Home Assistant

Unofficial **read-only** Home Assistant custom integration for the MOVA LumeGret A4000 and MOVA Smart Meter P1 via the MOVAhome EU cloud.

> This is a community project. It is not an official MOVA or Home Assistant integration. Cloud or firmware changes may require updates to this project.

## Supported / tested setup

This integration was developed and tested with:

- MOVA LumeGret A4000 (`mova.bkw.ge2505`)
- MOVA B4000 battery expansion in the test installation
- MOVA Smart Meter P1 (`mova.sme.ge2608`)
- MOVAhome EU account
- Home Assistant custom integrations

The B4000 is part of the tested battery system, but it is not exposed as a separate cloud device by this integration.

## Safety first: read-only

The public integration only reads telemetry. It does **not** include charging, discharging, mode-changing, or other battery-control writes.

The cloud client uses `get_properties` for telemetry. Experimental write/controller research is intentionally not part of this public repository.

## Entities

### MOVA LumeGret A4000

- Battery SoC
- Battery power
- Battery charging power
- Battery discharging power
- Battery current
- Battery direction
- Operating status

### MOVA Smart Meter P1

- Grid power
- Grid import
- Grid export

Power sign convention used by the integration:

- battery power: positive = discharging, negative = charging
- grid power: positive = import, negative = export

The cloud is polled every 10 seconds in this release.

## Installation

### HACS custom repository

This repository is structured for use as a HACS custom repository:

1. Open HACS.
2. Open the menu and choose **Custom repositories**.
3. Add `https://github.com/drosharold-coder/mova-lumegret-home-assistant`.
4. Choose **Integration** as the category.
5. Install **MOVA LumeGret Energy**.
6. Restart Home Assistant.
7. Go to **Settings -> Devices & services -> Add integration**.
8. Search for **MOVA LumeGret Energy**.
9. Sign in with the same MOVAhome account used by the official MOVAhome app.

### Manual installation

1. Create a Home Assistant backup.
2. Copy `custom_components/mova_lumegret` from this repository to:

```text
/config/custom_components/mova_lumegret/
```

3. Restart Home Assistant.
4. Add **MOVA LumeGret Energy** from **Settings -> Devices & services**.

Expected structure:

```text
/config/custom_components/mova_lumegret/
├── __init__.py
├── api.py
├── brand/
│   ├── icon.png
│   └── icon@2x.png
├── config_flow.py
├── const.py
├── coordinator.py
├── manifest.json
├── sensor.py
└── translations/
    ├── en.json
    └── nl.json
```

## Optional: Home Assistant Energy Dashboard

`optional/mova_energy_dashboard.yaml` creates cumulative kWh sensors from the live charge and discharge power sensors.

Before using it, check that these entity IDs exist in your Home Assistant installation:

```text
sensor.mova_lumegret_a4000_batterij_laden
sensor.mova_lumegret_a4000_batterij_ontladen
```

If packages are enabled, copy the file to for example:

```text
/config/packages/mova_energy_dashboard.yaml
```

Restart Home Assistant and add the resulting cumulative battery-energy sensors under **Settings -> Dashboards -> Energy -> Battery storage**.

## Credentials and privacy

The setup flow asks for the MOVAhome email address and password because the current integration authenticates against the MOVAhome cloud. Home Assistant stores config-entry data locally in the Home Assistant configuration storage. Do not share `.storage` files or diagnostics containing credentials.

The repository itself contains no personal account password, live access token, refresh token, cookie, personal device ID, or private LAN address.

## Known limitations

- Cloud dependent; this is not a local API integration.
- Tested against known EU MOVAhome behavior and the model IDs listed above.
- This release currently expects both an A4000 and Smart Meter P1 on the same MOVAhome account.
- Cloud endpoints and property behavior are unofficial and may change.
- The default 10-second polling interval is based on the tested installation; no official public MOVA cloud rate limit is documented here.

## Why this project exists

The goal is to make MOVA battery telemetry usable in Home Assistant today, share reproducible community experience, and provide a practical foundation for a future official MOVA Home Assistant/local API integration.

## Version

Current public release: **v0.1.3**

## License

MIT. MOVA names and trademarks remain the property of their respective owners. Any community artwork in this repository is not an official MOVA logo.
