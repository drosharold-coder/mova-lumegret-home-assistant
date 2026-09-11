# Supported devices

This page lists hardware that has been verified with the public read-only MOVA LumeGret Home Assistant integration.

## Verified hardware

| Product | Model ID | Status | Notes |
|---|---|---|---|
| MOVA LumeGret A4000 | `mova.bkw.ge2505` | Supported | Battery telemetry is exposed in Home Assistant. |
| MOVA B4000 expansion battery | n/a in this integration | Tested as part of the A4000 system | The B4000 is part of the tested battery stack, but it is not exposed as a separate MOVAhome cloud device by this integration. |
| MOVA Smart Meter P1 | `mova.sme.ge2608` | Supported | Grid power, import and export telemetry are exposed. |

## A4000 entities

The integration currently exposes:

- Battery SoC
- Battery power
- Battery charging power
- Battery discharging power
- Battery current
- Battery direction
- Operating status

## Smart Meter P1 entities

The integration currently exposes:

- Grid power
- Grid import
- Grid export

## Sign convention

- Battery power: positive = discharging, negative = charging
- Grid power: positive = import, negative = export

## Other MOVA models

Other MOVA energy products are not automatically assumed to be compatible. Before adding a device we want to verify:

1. the MOVAhome model ID;
2. whether the device appears in the same EU cloud account;
3. which telemetry properties are returned;
4. unit/sign behavior;
5. that the public implementation remains read-only.

If you own another MOVA energy product, open an issue and include the product name, Home Assistant version and non-sensitive diagnostic information. Never post passwords, tokens, cookies, addresses or personal device identifiers.
