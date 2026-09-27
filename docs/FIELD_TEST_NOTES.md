# Sanitized field-test notes

This page records **high-level, privacy-safe findings** from the MOVA + Home Assistant engineering tests. It deliberately does not contain private configuration, device identifiers, addresses, IPs, credentials or controller source code.

## Test purpose

The practical tests are intended to answer whether a central Home Assistant EMS can coordinate:

- MOVA A4000/B4000 telemetry;
- MOVA Smart Meter P1 grid measurements;
- another home-battery system;
- household demand;
- solar surplus;
- dynamic price/deadline planning;

without the battery systems unnecessarily working against each other.

## Findings so far

### Read-only telemetry

The public MOVA integration has proven useful as a reliable common telemetry layer for:

- battery state of charge;
- battery charge/discharge power;
- grid import/export;
- operating state.

### Multi-battery coordination

The test installation demonstrates that MOVA can be monitored alongside a battery from another manufacturer in Home Assistant.

The important design principle is that **Home Assistant / the EMS is the common coordination layer**. This is not an official MOVA-to-third-party protocol.

### Solar surplus

Solar-surplus charging has been part of the practical tests. The goal is to use local PV energy for household demand and battery charging before unnecessary grid export, while preventing one battery from charging from energy that another battery is simultaneously discharging.

### High-load behaviour

High household loads are a separate test case because battery limits and response times can otherwise cause short grid-import peaks. Stabilization logic is therefore treated as an explicit part of the EMS design.

### Grid charging and price planning

Price/deadline planning is still being refined. Tests have shown that a controller can be technically correct while still making economically undesirable grid-charging decisions if timing, expected PV and remaining energy need are not considered carefully enough.

This remains an active engineering area and is **not presented as finished public controller functionality**.

### SELL / export control

Future SELL behaviour is being validated in shadow/simulation first. Shadow logic may calculate a theoretical sell action, but it does not itself actuate the batteries.

SELL should only move from shadow to public control after enough real price windows and safety cases have been observed.

## Publication rule

A feature should only be labelled **tested** after representative practical operation. A feature that has only been simulated, shadowed or code-reviewed should be labelled **experimental**, **shadow** or **not yet validated**.

## Safety / privacy

No full Home Assistant backup, local recovery archive, token, password, serial number, private IP or other identifying installation detail should be used as a public test artifact.
