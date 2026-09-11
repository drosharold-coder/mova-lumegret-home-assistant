# Troubleshooting

## Integration cannot be found

1. Confirm that `custom_components/mova_lumegret/` exists in the Home Assistant config directory.
2. If installed through HACS, confirm the repository is added as an **Integration** custom repository.
3. Restart Home Assistant after installation or update.
4. Check **Settings -> System -> Logs** for `mova_lumegret` errors.

## Login fails

- Use the same MOVAhome EU account that works in the official MOVAhome app.
- Re-enter the email address and password carefully.
- Confirm the MOVAhome app itself can currently reach the account/cloud.
- Do not post credentials in a GitHub issue.

## No devices are found

This release is tested with an A4000 and Smart Meter P1 in the same MOVAhome account. If your account contains different hardware, please open a device-support issue instead of sharing private cloud responses publicly.

## Sensors show `unavailable`

1. Check that the internet connection works.
2. Check whether the official MOVAhome app shows live data.
3. Restart Home Assistant once.
4. Reload the MOVA LumeGret integration from **Settings -> Devices & services**.
5. Check Home Assistant logs for connection/authentication errors.

The integration is cloud-polling; a MOVAhome cloud outage can therefore make entities temporarily unavailable.

## Values look reversed

The integration uses these sign conventions:

- Battery power: positive = discharging, negative = charging.
- Grid power: positive = import, negative = export.

Separate charge/discharge and import/export entities are provided to make dashboards easier to understand.

## `icon not available`

Update Home Assistant to a recent release, update/reinstall the custom integration and restart Home Assistant. The project currently uses community artwork; official MOVA branding will only be used if MOVA explicitly permits it and supplies/approves the asset.

## HACS still shows an old version

- Refresh HACS information.
- Confirm you are using `drosharold-coder/mova-lumegret-home-assistant`.
- Update the integration in HACS.
- Restart Home Assistant.
- Check the version shown on the integration page again.

## Energy Dashboard package does not work

The optional package depends on the live charging/discharging entity IDs. Verify your actual entity IDs before copying the package. See `docs/DASHBOARD.md` and `optional/mova_energy_dashboard.yaml`.

## Before opening an issue

Please include:

- Home Assistant Core version;
- integration version;
- MOVA product/model;
- whether MOVAhome itself is online;
- a short description of expected vs actual behavior;
- relevant Home Assistant log lines with credentials, tokens, addresses and device identifiers removed.
