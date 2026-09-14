<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="custom_components/mova_lumegret/brand/dark_logo.png">
    <img alt="MOVA" src="custom_components/mova_lumegret/brand/logo.png" width="520">
  </picture>
</p>

# MOVA LumeGret Energy for Home Assistant

Unofficial **read-only** Home Assistant custom integration for the MOVA LumeGret A4000 and MOVA Smart Meter P1 via the MOVAhome EU cloud.

> This is a community project. It is not an official MOVA or Home Assistant integration. Cloud or firmware changes may require updates to this project.
>
> **Branding:** MOVA has granted permission to use the official MOVA/LumeGret logo for this community Home Assistant integration on GitHub and HACS. The integration itself remains unofficial and community-maintained.

## Documentation

- [Detailed installation guide](docs/INSTALLATION.md)
- [Nederlandse installatiehandleiding](docs/INSTALLATION_NL.md)
- [Supported devices](SUPPORTED_DEVICES.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [FAQ](FAQ.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Dashboard / Energy Dashboard](docs/DASHBOARD.md)
- [Multi-brand battery setups](docs/MULTI_BATTERY.md)
- [Nederlandse uitleg: meerdere accumerken](docs/MULTI_BATTERY_NL.md)
- [Test matrix & release checklist](docs/TEST_MATRIX.md)
- [Roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

## Supported / tested setup

This integration was developed and tested with:

- MOVA LumeGret A4000 (`mova.bkw.ge2505`)
- MOVA B4000 battery expansion in the test installation
- MOVA Smart Meter P1 (`mova.sme.ge2608`)
- MOVAhome EU account
- Home Assistant custom integrations

The B4000 is part of the tested battery system, but it is not exposed as a separate cloud device by this integration.

## Home Assistant preview

The previews below are privacy-safe recreations based on screenshots from the real test installation. Personal addresses and unrelated private automations have deliberately been left out.

### Integration overview

![MOVA LumeGret integration overview](docs/images/mova-integration-overview.svg)

### MOVA LumeGret A4000

![MOVA LumeGret A4000 in Home Assistant](docs/images/mova-a4000-home-assistant.svg)

### MOVA Smart Meter P1

![MOVA Smart Meter P1 in Home Assistant](docs/images/mova-p1-home-assistant.svg)

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

For screenshots, updating and manual installation, see [the detailed installation guide](docs/INSTALLATION.md).

## Optional: Home Assistant Energy Dashboard

`optional/mova_energy_dashboard.yaml` creates cumulative kWh sensors from the live charge and discharge power sensors.

Before using it, check that these entity IDs exist in your Home Assistant installation:

```text
sensor.mova_lumegret_a4000_batterij_laden
sensor.mova_lumegret_a4000_batterij_ontladen
```

See [Dashboard / Energy Dashboard](docs/DASHBOARD.md) for the full setup.

## Multi-brand battery setups

MOVA telemetry can be used in the same Home Assistant installation as telemetry from a home battery of another manufacturer. Home Assistant can then provide one common monitoring layer, and a separate EMS can coordinate multiple systems if reliable writable interfaces are available for the batteries involved.

This is a Home Assistant / EMS architecture pattern, **not** a claim of official MOVA-to-third-party compatibility. This public MOVA integration remains read-only and does not coordinate charging or discharging itself.

See [Multi-brand battery setups](docs/MULTI_BATTERY.md) for the architecture, conflict-avoidance rules and validation checklist.

## Credentials and privacy

The setup flow asks for the MOVAhome email address and password because the current integration authenticates against the MOVAhome cloud. Home Assistant stores config-entry data locally in the Home Assistant configuration storage. Do not share `.storage` files or diagnostics containing credentials.

The repository itself contains no personal account password, live access token, refresh token, cookie, personal device ID, or private LAN address.

## Known limitations

- Cloud dependent; this is not a local API integration.
- Tested against known EU MOVAhome behavior and the model IDs listed above.
- This release currently expects both an A4000 and Smart Meter P1 on the same MOVAhome account.
- Cloud endpoints and property behavior are unofficial and may change.
- The default 10-second polling interval is based on the tested installation; no official public MOVA cloud rate limit is documented here.
- Local custom-integration brand images require a recent Home Assistant release. If Home Assistant shows `icon not available`, first update Home Assistant and reinstall/update this integration before troubleshooting the artwork itself.

## Why this project exists

The goal is to make MOVA battery telemetry usable in Home Assistant today, share reproducible community experience, and provide a practical foundation for a future official MOVA Home Assistant/local API integration.

## Version

Current public release: **v0.1.3**

Next release in preparation: **v0.1.4**

## License and trademarks

MIT. MOVA names, logos and trademarks remain the property of their respective owners. The official MOVA/LumeGret logo is used with permission for this community Home Assistant integration on GitHub and HACS; that permission does not make the integration an official MOVA product.
