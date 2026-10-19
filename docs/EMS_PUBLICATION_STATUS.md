# Public EMS / controller publication status

This repository publishes the **read-only MOVA Home Assistant integration** plus privacy-safe documentation from the wider energy-management project.

The private Home Assistant EMS/controller is intentionally kept separate from the integration.

## Current status — October 2026

The private engineering system has evolved into a coordinated multi-battery EMS rather than a single experimental control loop.

The primary real-world test site includes:

- MOVA battery storage;
- a second battery platform;
- **19.52 kWh total nominal storage**;
- a central household / near-zero-grid control objective;
- solar-surplus coordination;
- high-load support;
- state-of-charge and reserve management;
- battery failover and recovery;
- price-aware charging;
- export/SELL planning under continued validation.

The public MOVA integration still performs telemetry only.

## What is already public

- Read-only A4000 telemetry.
- Read-only MOVA Smart Meter P1 telemetry.
- B4000 documentation as part of the tested A4000 stack.
- Installation and troubleshooting documentation.
- Energy Dashboard guidance.
- Multi-brand battery architecture documentation.
- Conflict-avoidance and validation guidance.
- Privacy-safe field-test notes.
- Public EMS bundle and test-report plans.

## What has now been demonstrated privately

Representative practical operation has demonstrated:

- one Home Assistant EMS can coordinate MOVA and another battery platform;
- solar surplus can be used as an EMS input for battery decisions;
- high-load behaviour needs explicit stabilization;
- battery availability can change during operation and requires failover;
- the remaining battery system can support the house during a battery/network availability incident;
- recovery must return the system to one known controller state;
- price-aware charging needs expected demand and expected solar production, not tariff alone.

A second community test environment in France is also being prepared around multiple MOVA A4000 units and B4000 expansion for future cross-installation validation.

## Still not a public production controller

The following remain outside the public integration and must not be presented as finished public functionality:

- installation-specific write commands;
- private controller packages;
- experimental export/SELL actuation that has not completed sufficient practical validation;
- reverse-engineering captures containing identifiers;
- recovery archives or full Home Assistant backups.

## Publication gate for controller code

Controller code should only become public after it is:

1. stable over representative practical operation;
2. separated from local/private Home Assistant configuration;
3. stripped of IP addresses, serial numbers, credentials, tokens and personal identifiers;
4. converted to generic documented configuration;
5. supplied with safe defaults, bounds and stale-data handling;
6. checked for battery-to-battery conflict behaviour;
7. re-tested after sanitization so the public version is proven, not merely copied.

## Files that must never be published

Do **not** upload:

- full Home Assistant backups;
- local recovery archives;
- private IP addresses or MAC addresses;
- credentials, tokens, cookies or cloud identifiers;
- personal device identifiers or serial numbers;
- private logs containing identifying data;
- unrelated installation-specific packages.

## Repository separation

The MOVA integration should remain a clean read-only project.

A future writable multi-battery EMS/controller should be published as a clearly separate package or repository so users cannot confuse community EMS control with official MOVA integration behaviour.
