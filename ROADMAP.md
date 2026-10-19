# Roadmap

This roadmap describes the intended direction of the community integration. It is not a promise of official MOVA support or delivery dates.

## Current focus

- Keep the public integration read-only.
- Maintain reliable A4000 and Smart Meter P1 telemetry.
- Complete the practical HACS/update validation before the next release.
- Keep privacy and read-only CI guards in place.
- Document real multi-battery/EMS findings without publishing private controller code.
- Use the approved MOVA/LumeGret branding consistently.

## Near term

- Clean HACS install/update verification for the next release.
- Bring the v0.1.4 hardening work up to date with current main.
- Validate privacy-safe diagnostics and cloud retry behaviour on the real test installation.
- Investigate the A4000 direct PV inputs requested by the community:
  - PV1 power;
  - PV2 power;
  - PV3 power;
  - PV4 power;
  - total PV power;
  - later, cumulative PV energy if reliable source data is available.
- Improve Energy Dashboard support with native/validated energy statistics where possible.

## Community validation

- Expand testing beyond the original Dutch installation.
- Validate a second community setup in France with multiple A4000 units and B4000 expansion.
- Record model, firmware and Home Assistant behaviour without publishing account/device identifiers.
- Only mark additional hardware combinations as supported after real-device validation.

## Medium term

- Test additional MOVA energy-storage products when hardware/model IDs become available.
- Improve diagnostics and troubleshooting around cloud/session failures.
- Continue documenting vendor-independent Home Assistant EMS architecture.
- Prepare a **separate sanitized EMS preview** only after the public version has been re-tested independently from the private installation.
- Add translations from community contributions.

## Preferred long-term direction

- Official/documented MOVA API support.
- Preferably a local LAN API so Home Assistant can work without cloud dependency.
- Stable device discovery and documented telemetry/control fields.
- Official Home Assistant/MOVA collaboration if MOVA wishes to support it.
- Broader real-world testing across multiple households, battery combinations and energy scenarios.

## Not planned for the public integration

- Experimental battery write/control commands.
- Full private Home Assistant packages or backups.
- Publishing reverse-engineering captures containing personal identifiers.
- Publishing account tokens, cookies, credentials or LAN details.

Experimental control/EMS work may continue separately for engineering/testing, but it remains intentionally outside the public read-only integration.
