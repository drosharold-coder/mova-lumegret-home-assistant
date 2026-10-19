# Test matrix

This file records what has actually been verified. A product or sensor should not be marked supported based only on a model name, app screen or specification sheet.

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
| Multi-brand architecture | MOVA + second battery platform under one HA EMS | ✅ Real-world validated | EMS layer is separate from this read-only integration. |
| Failover concept | Continue with remaining battery after battery/network loss | ✅ Real-world observed | Recovery remains part of ongoing validation. |
| External validation | Multiple A4000 units + B4000 in second household | 🧪 In preparation | Community test site in France; not yet marked supported. |
| A4000 PV inputs | PV1–PV4 power | 🔎 Investigation requested | Tracked by community issue; not in v0.1.3. |
| A4000 PV total | Total PV power / energy | 🔎 Investigation requested | Requires verified read-only properties first. |
| Home Assistant validation | Hassfest | ✅ Previously passing | Re-check on the final next-release head. |
| HACS validation | HACS action | ✅ Previously passing | Re-check on the final next-release head. |
| Public safety guard | Read-only check | ✅ Guard present | Public integration must not contain battery-control writes. |
| HACS clean update | v0.1.3 -> next release | ⏳ Pending | Required before publishing v0.1.4. |
| Branding permission | Official MOVA/LumeGret assets | ✅ Confirmed for project | Integration remains unofficial/community-maintained. |
| Branding display | Custom icon on current HA | ⏳ Practical verification | Re-check during HACS/update test. |

## Release checklist

Before a new public release:

- [ ] Install/update through HACS on the real test system.
- [ ] Restart Home Assistant.
- [ ] Confirm the displayed integration version.
- [ ] Confirm A4000 entities update.
- [ ] Confirm P1 import/export updates.
- [ ] Check Home Assistant logs for unexpected errors.
- [ ] Verify diagnostics do not expose credentials or private identifiers.
- [ ] Confirm no secrets/private identifiers were added to the repository.
- [ ] Confirm read-only guard passes.
- [ ] Confirm HACS validation passes.
- [ ] Confirm Hassfest passes.
- [ ] Update `CHANGELOG.md`.
- [ ] Update this test matrix for any newly verified sensors/devices.

## Community testing

If you test another MOVA product or a second installation, report the exact product/model and Home Assistant version, but sanitize all account/device identifiers before posting anything publicly.
