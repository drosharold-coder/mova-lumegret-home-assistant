# Sanitized field-test notes

This page records **high-level, privacy-safe findings** from real MOVA + Home Assistant energy-management testing. It does not contain private configuration, device identifiers, addresses, IPs, credentials or controller source code.

## Test environment

The primary test installation currently combines MOVA storage with a second home-battery platform under one Home Assistant EMS.

Combined nominal battery capacity in the test environment is **19.52 kWh**.

The EMS uses household/grid power, battery state, solar conditions and energy-price information as inputs. The public MOVA integration remains read-only; writable EMS control is a separate private engineering layer.

## Findings so far

### Read-only MOVA telemetry

The public integration has proven useful as a common telemetry layer for:

- battery state of charge;
- battery charge/discharge power;
- battery current/direction/status;
- Smart Meter P1 grid import/export.

### Multi-battery coordination

The real installation demonstrates that MOVA can participate in the same Home Assistant EMS as a battery from another manufacturer.

The important design principle is that **Home Assistant / the EMS is the common coordination layer**. This is not an official MOVA-to-third-party protocol.

A stable design needs one owner for the household/grid-power target. Independent battery controllers reacting to the same signal can otherwise work against each other.

### Solar surplus

Solar-surplus behaviour is part of the practical control strategy.

The objective is to use local PV energy for household demand and battery charging before unnecessary grid export, while avoiding unintended battery-to-battery energy transfer.

### High-load behaviour

High household loads remain an explicit test case because battery limits, communication delay and controller response time can create short grid-import peaks.

The practical result is that high-load stabilization should be treated as its own control problem rather than assuming the normal low-load loop will always respond optimally.

### Battery failover and recovery

A real MOVA/network availability incident provided a practical failover test.

The EMS continued household support through the remaining battery system and recovery behaviour was checked after the unavailable system returned.

This confirmed an important design requirement: failover is not complete until recovery also returns control to one known, non-competing state.

### Price-aware charging

Price planning has progressed beyond simple “charge when cheap” logic.

Testing showed that tariff alone is not enough. Useful planning also needs to consider:

- current SoC;
- reserve requirement;
- expected household consumption;
- expected solar production;
- remaining time before the energy is needed;
- practical battery power/capacity constraints.

### Export / SELL planning

Export/SELL planning remains under active validation.

The project continues to separate planning/shadow logic from any behaviour that would be described publicly as proven unattended SELL control.

### Second test installation

A community tester in France is preparing a setup with multiple MOVA A4000 units and B4000 expansion.

This gives the project an opportunity to validate telemetry and future integration behaviour on a second household installation rather than relying on one test site.

No tester identity, address, account data, serial number or private network information should be published.

### Direct PV inputs

A community feature request is now tracking read-only PV1–PV4 input-power sensors for the A4000.

Those sensors are not yet part of the released integration and should not be described as supported until the properties are identified and verified on real hardware.

## Publication rule

A feature should only be labelled **tested** after representative practical operation.

A feature that has only been simulated, shadowed, code-reviewed or observed on one unverified property should be labelled **experimental**, **shadow**, **candidate** or **not yet validated**.

## Safety / privacy

No full Home Assistant backup, local recovery archive, token, password, serial number, private IP or other identifying installation detail should be used as a public test artifact.
