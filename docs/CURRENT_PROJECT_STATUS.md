# Current project status — October 2026

This page gives a privacy-safe snapshot of where the MOVA / Home Assistant project stands today.

## Public integration

The public MOVA LumeGret Home Assistant integration remains deliberately **read-only**.

Current public release:

- **v0.1.3**
- MOVA LumeGret A4000 telemetry
- MOVA Smart Meter P1 grid telemetry
- B4000 validated as part of the A4000 battery stack
- HACS custom-repository installation
- English and Dutch documentation
- official MOVA/LumeGret branding used with permission

The next integration release is still being prepared and will not be published until the practical HACS/update validation is completed.

## Real-world EMS test site

The private engineering environment has developed well beyond the first proof-of-concept.

The primary test installation currently combines:

- MOVA battery storage;
- a second battery platform;
- **19.52 kWh total nominal storage** across both systems;
- Home Assistant as the common monitoring and EMS layer;
- one common household/grid-power reference;
- solar-surplus coordination;
- reserve and state-of-charge management;
- high-load behaviour;
- battery failover/recovery;
- price-aware charging and export planning.

The public MOVA integration itself does not perform these write/control actions. The EMS/controller layer remains separate.

## Multi-brand result

The project has now demonstrated in real daily operation that Home Assistant can act as a common coordination layer for battery systems from different manufacturers.

This is **not** an official MOVA-to-third-party battery protocol. The value is in the higher-level Home Assistant architecture: each battery keeps its own interface, while one EMS coordinates the overall household objective.

Important design lessons include:

- one controller should own the household/grid-power target;
- batteries need explicit priorities and SoC boundaries;
- failover must not create a second competing controller;
- stale or unavailable telemetry needs a safe fallback;
- charging one battery while another is discharging should be prevented unless explicitly intended;
- price optimization must include expected household demand and solar production, not just the current tariff.

## Failover testing

A real battery/network availability incident was used to test recovery behaviour.

The EMS was able to continue household support with the remaining battery platform and later recover when the unavailable system returned. This has made failover and recovery a first-class part of the project rather than only a theoretical feature.

## Second-site community validation

A second community test environment in France is being prepared around **multiple MOVA A4000 units with B4000 expansion**.

This is important because it allows future validation outside the original Dutch test installation and can help distinguish installation-specific behaviour from repeatable MOVA behaviour.

No personal account data, addresses, serial numbers or private network details from community testers should be published.

## New telemetry work

Community feedback has also identified interest in the A4000's direct PV inputs.

Tracking is open for:

- PV1 power;
- PV2 power;
- PV3 power;
- PV4 power;
- total PV power;
- future cumulative PV energy for the Home Assistant Energy Dashboard.

These sensors should only be added after the relevant read-only properties have been identified and validated on real hardware.

## Public EMS direction

The long-term public goal is a separate **sanitized EMS preview**, not a dump of the private Home Assistant installation.

A public EMS package should contain only generic configuration, documented placeholders, safe defaults, clear failure behaviour and functions that have been validated in representative practical operation.

Experimental export/SELL behaviour must remain clearly labelled until practical validation is sufficient.

## Project principle

The project has moved from:

**“Can MOVA data be shown in Home Assistant?”**

to:

**“How can MOVA participate safely and effectively in a complete, vendor-independent residential energy-management system?”**
