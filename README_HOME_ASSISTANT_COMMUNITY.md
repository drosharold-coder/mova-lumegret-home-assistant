# Home Assistant Community post

## MOVA LumeGret A4000 + Smart Meter P1 custom integration

I have published an unofficial **read-only** Home Assistant custom integration for the MOVA LumeGret A4000 and MOVA Smart Meter P1.

MOVA has granted permission to use the official MOVA/LumeGret logo for this community Home Assistant integration on GitHub and HACS. The integration itself remains unofficial and community-maintained.

Tested public-integration setup:

- MOVA LumeGret A4000 (`mova.bkw.ge2505`)
- B4000 battery expansion in the test installation
- MOVA Smart Meter P1 (`mova.sme.ge2608`)
- MOVAhome EU account

The integration exposes battery SoC, battery power, charging/discharging power, battery current, battery direction and operating status, plus Smart Meter P1 grid power, import and export.

The public integration is deliberately read-only. It does not contain battery charge/discharge commands, mode changes or experimental write/EMS control logic.

The wider project has now also validated a **vendor-independent multi-battery Home Assistant EMS architecture** in real daily use, with 19.52 kWh combined nominal storage across MOVA and a second battery platform. That EMS/control work is separate from this repository's read-only integration.

A second community validation site in France with multiple A4000 units and B4000 expansion is being prepared. It will not be marked supported until practical testing is complete.

Community feedback is also tracking future read-only PV1–PV4 and total PV-power sensors for the A4000.

GitHub repository:
https://github.com/drosharold-coder/mova-lumegret-home-assistant

Current public release: **v0.1.3**

The next release remains in preparation until the practical HACS/update validation has been completed.

Feedback and additional MOVA model testing are welcome through GitHub Issues. Please do not post passwords, tokens, addresses, private device IDs or Home Assistant `.storage` contents.
