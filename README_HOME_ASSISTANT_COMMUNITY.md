# Home Assistant Community post

## MOVA LumeGret A4000 + Smart Meter P1 custom integration

I have published an unofficial **read-only** Home Assistant custom integration for the MOVA LumeGret A4000 and MOVA Smart Meter P1.

Tested setup:

- MOVA LumeGret A4000 (`mova.bkw.ge2505`)
- B4000 battery expansion in the test installation
- MOVA Smart Meter P1 (`mova.sme.ge2608`)
- MOVAhome EU account

The integration exposes battery SoC, battery power, charging/discharging power, battery current, battery direction and operating status, plus Smart Meter P1 grid power, import and export.

The public integration is deliberately read-only. It does not contain battery charge/discharge commands, mode changes or experimental write/EMS control logic.

The current implementation uses MOVAhome cloud polling and is not an official MOVA integration. Cloud or firmware changes may require updates.

GitHub repository:
https://github.com/drosharold-coder/mova-lumegret-home-assistant

Current public release: **v0.1.3**

Installation is possible through HACS as a custom repository or manually by copying `custom_components/mova_lumegret` into Home Assistant. The repository also contains English/Dutch documentation, privacy-safe Home Assistant previews, troubleshooting, supported-device information, test matrix, roadmap and an optional Energy Dashboard package.

Feedback and additional MOVA model testing are very welcome through GitHub Issues. Please do not post passwords, tokens, addresses, private device IDs or Home Assistant `.storage` contents.
