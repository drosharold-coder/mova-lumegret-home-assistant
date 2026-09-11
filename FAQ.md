# FAQ

## Is this an official MOVA integration?

No. This is an independent community integration. MOVA names and trademarks remain the property of their respective owners.

## Is it read-only?

Yes. The public repository only reads telemetry. It does not contain public charging, discharging, mode-changing or other battery-control writes.

## Does it work locally?

Not yet. The current integration uses the MOVAhome EU cloud. A documented/official local API would be preferred in the future if MOVA makes one available.

## Which devices are supported?

The verified setup is MOVA LumeGret A4000 + B4000 expansion + MOVA Smart Meter P1. See `SUPPORTED_DEVICES.md` for the exact model IDs and behavior.

## Why is the B4000 not shown as a separate Home Assistant device?

In the tested MOVAhome setup, the B4000 functions as an expansion battery for the A4000 and is not exposed to this integration as a separate cloud device.

## Do I need the Smart Meter P1?

The current public release was tested with both the A4000 and Smart Meter P1 in the same account. The integration currently expects that tested setup.

## How often is data updated?

The current integration polls the cloud every 10 seconds.

## Can I use it in the Home Assistant Energy Dashboard?

Yes, with the optional package in `optional/mova_energy_dashboard.yaml`. It converts live battery charge/discharge power into cumulative kWh sensors suitable for the Energy Dashboard.

## Why does Home Assistant show `icon not available`?

First update Home Assistant and the integration, then restart Home Assistant. The project uses community artwork unless/until MOVA grants explicit permission for official branding.

## Will future MOVA firmware/cloud changes break it?

They may. The cloud interface used by this community integration is not an official public API contract. Compatibility updates may be needed after MOVA firmware/cloud changes.

## Can I contribute support for another MOVA model?

Yes. Please open an issue first and do not upload credentials, tokens, cookies, addresses or unique personal device identifiers.

## Where is the experimental EMS/write control?

It is intentionally not published in this repository. The public project is kept read-only so users can inspect telemetry without exposing experimental battery-control code.
