# EMS public bundle plan

This document defines the **sanitized public bundle** that may be published after the private multi-battery EMS has passed the remaining practical tests.

The goal is to make the project useful to other Home Assistant users without exposing installation-specific data or presenting experimental functions as production-ready.

## Scope of the first public preview

The first public EMS preview should focus on the parts that can be explained and validated safely:

- central household / grid-power target;
- multi-battery coordination principles;
- solar-surplus charging strategy;
- high-load stabilization;
- state-of-charge limits;
- anti-conflict logic so batteries do not intentionally charge and discharge against each other;
- safe fallback behaviour when a data source or controller is unavailable.

## Keep separate from the MOVA integration

The existing MOVA custom integration stays **read-only**.

A future EMS/controller bundle should be published as a clearly separate layer. This avoids giving users the impression that the MOVA integration itself performs battery-control writes.

## Planned directory structure

A sanitized bundle could use a structure like:

```text
ems-public-preview/
├── README.md
├── CHANGELOG.md
├── configuration.example.yaml
├── packages/
│   └── multi_battery_ems.example.yaml
├── docs/
│   ├── ARCHITECTURE.md
│   ├── INSTALLATION.md
│   ├── TESTING.md
│   └── SAFETY.md
└── examples/
    └── dashboard.example.yaml
```

The filenames above describe the intended public package only. They are not a copy of the private Home Assistant installation.

## Sanitization requirements

Before any private controller file is copied into the public bundle:

- remove private IP addresses;
- remove MAC addresses and serial numbers;
- remove account IDs, device IDs and cloud identifiers;
- remove tokens, passwords, cookies and secrets;
- remove names, addresses and other personal information;
- replace installation-specific entity IDs with documented placeholders where practical;
- remove unrelated local packages/automations;
- remove recovery and backup paths;
- check comments and logs for private data as well as executable configuration.

## Feature maturity labels

Every public feature should have one of these labels:

- **Tested** — validated during representative practical operation.
- **Preview** — working in practice but still being tuned.
- **Shadow** — calculates or simulates actions but does not actuate hardware.
- **Experimental** — engineering work; not recommended for unattended use.
- **Not public** — private/local implementation only.

A feature should never be promoted from Shadow or Experimental to Tested based only on code inspection.

## Initial safety defaults

A public controller should default to conservative behaviour:

- no SELL/export actuation unless explicitly enabled;
- no aggressive grid charging by default;
- clear minimum and maximum SoC boundaries;
- bounded power commands;
- stale-data detection;
- safe fallback when Home Assistant, cloud telemetry or a battery interface is unavailable;
- no assumption that two different battery brands use the same sign convention or control semantics.

## Release gate

Before publishing a first EMS preview:

1. run the practical test set again on the final sanitized code;
2. verify that removal of private/local dependencies did not change behaviour;
3. review the bundle for secrets and identifiers;
4. confirm all example entity IDs are generic/documented;
5. mark SELL/shadow functionality accurately;
6. publish the bundle as a preview, not as an official MOVA feature.

## Important

The public EMS work is a community Home Assistant project. It is not an official MOVA controller and does not imply official interoperability between MOVA and another battery manufacturer.
