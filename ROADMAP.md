# Roadmap

This roadmap describes the intended direction of the community integration. It is not a promise of official MOVA support or delivery dates.

## Current focus

- Keep the public integration read-only.
- Maintain reliable A4000 and Smart Meter P1 telemetry.
- Keep HACS and Home Assistant validation green.
- Improve installation and troubleshooting documentation.
- Validate updates with a real Home Assistant installation before publishing releases.

## Near term

- Clean HACS install/update verification for the next release.
- Improve onboarding screenshots and dashboard examples.
- Add clearer diagnostics that avoid exposing credentials or personal identifiers.
- Confirm/repair custom branding behavior on current Home Assistant releases.
- Use official MOVA/LumeGret artwork only if MOVA explicitly approves its use.

## Medium term

- Test additional MOVA energy-storage products when hardware/model IDs become available.
- Support additional models only after real-device validation.
- Improve energy statistics and Home Assistant Energy Dashboard integration.
- Document and validate multi-brand Home Assistant battery setups without moving experimental write/control logic into this public integration.
- Add translations from community contributions.

## Preferred long-term direction

- Official/documented MOVA API support.
- Preferably a local LAN API so Home Assistant can work without cloud dependency.
- Stable device discovery and documented telemetry fields.
- Official Home Assistant/MOVA collaboration if MOVA wishes to support it.

## Not planned for the public repository right now

- Experimental battery write/control commands.
- Publishing private reverse-engineering captures containing personal device identifiers.
- Publishing account tokens, cookies, credentials or LAN details.

Experimental control/EMS work may exist separately for engineering/testing, but it is intentionally outside this public read-only project.
