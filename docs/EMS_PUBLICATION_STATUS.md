# Public EMS / controller publication status

This repository currently publishes the **read-only MOVA Home Assistant integration** and documentation around multi-brand battery architectures.

The separate Home Assistant EMS/controller work used in the private test installation is **not part of the public integration yet**.

## What is public now

- Read-only A4000 telemetry.
- Read-only MOVA Smart Meter P1 telemetry.
- Installation and troubleshooting documentation.
- Energy Dashboard guidance.
- Multi-brand battery architecture documentation.
- Conflict-avoidance and validation guidance.

## What has been tested privately

Several practical test days have been used to validate the central multi-battery concept in a real Home Assistant installation.

The private engineering setup has included:

- a central HOUSE / net-zero style control loop;
- high-load stabilization;
- coordination of MOVA with another home-battery system;
- solar-surplus charging logic;
- price/deadline planning;
- SELL logic in shadow/simulation before any real actuation.

These tests have been useful for finding both working behaviour and edge cases. In particular, grid-charging decisions and future SELL behaviour still require careful validation before controller code is suitable for public use.

## Why the controller code is not uploaded yet

The public repository should not contain experimental write/control logic before it is:

1. stable over representative practical test days;
2. separated from local/private Home Assistant configuration;
3. stripped of IP addresses, serial numbers, credentials, tokens and personal identifiers;
4. converted to generic configuration;
5. documented with clear safety limits and fallback behaviour;
6. checked so that multiple batteries cannot unintentionally charge and discharge against each other.

The public MOVA integration itself therefore remains **read-only**.

## Files that must never be published

Do **not** upload:

- full Home Assistant backups;
- local package archives used for recovery;
- private IP addresses;
- account credentials, tokens or cookies;
- personal device identifiers or serial numbers;
- private logs containing identifying data;
- installation-specific packages that have not been sanitized.

## Planned sanitized public bundle

When the controller work is considered ready, the public bundle should contain only:

- generic Home Assistant examples;
- a clear README;
- a changelog;
- safe defaults;
- documented entities / placeholders;
- a validation checklist;
- only functions that have been proven in practical testing.

Experimental or shadow-only functions should be marked as such and kept disabled by default.

## Repository separation

To avoid confusion, the read-only MOVA integration and a future writable multi-battery EMS/controller should remain clearly separated. A future EMS package may be published separately rather than being mixed into the core integration.
