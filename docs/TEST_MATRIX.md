# Test matrix

This file records what has actually been verified. A product should not be marked supported based only on a model name or specification sheet.

| Area | Hardware / function | Status | Notes |
|---|---|---|---|
| Device discovery | MOVA LumeGret A4000 | ✅ Verified | Model ID `mova.bkw.ge2505`. |
| Device discovery | MOVA Smart Meter P1 | ✅ Verified | Model ID `mova.sme.ge2608`. |
| Expansion battery | MOVA B4000 | ✅ Verified as part of A4000 stack | Not exposed as a separate cloud device in the current integration. |
| Battery telemetry | SoC | ✅ Verified | Live value visible in Home Assistant. |
| Battery telemetry | Charge/discharge power | ✅ Verified | Separate entities available. |
| Battery telemetry | Current/direction/status | ✅ Verified | Visible in Home Assistant. |
| Grid telemetry | Net power | ✅ Verified | Positive import / negative export convention. |
| Grid telemetry | Import/export split | ✅ Verified | Separate entities available. |
| Home Assistant validation | Hassfest | ✅ Passing | GitHub Actions. |
| HACS validation | HACS action | ✅ Passing | GitHub Actions. |
| Public safety guard | Read-only check | ✅ Passing | Public integration must not contain `set_properties` write control. |
| HACS clean update | v0.1.3 -> next release | ⏳ Pending | Run before publishing v0.1.4. |
| Branding | Custom icon on current HA | ⏳ To verify | Official MOVA artwork only after explicit permission. |

## Release checklist

Before a new public release:

- [ ] Install/update through HACS on the real test system.
- [ ] Restart Home Assistant.
- [ ] Confirm the displayed integration version.
- [ ] Confirm A4000 entities update.
- [ ] Confirm P1 import/export updates.
- [ ] Check Home Assistant logs for unexpected errors.
- [ ] Confirm no secrets/private identifiers were added.
- [ ] Confirm read-only guard passes.
- [ ] Confirm HACS validation passes.
- [ ] Confirm Hassfest passes.
- [ ] Update `CHANGELOG.md`.

## Community testing

If you test another MOVA product, report the exact product/model and Home Assistant version, but sanitize all account/device identifiers before posting anything publicly.
