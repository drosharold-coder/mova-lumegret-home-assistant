# Public EMS test report template

Use this template for privacy-safe practical validation before a controller feature is published.

## Test metadata

- Date:
- Home Assistant version:
- EMS/public preview version:
- MOVA integration version:
- Battery systems tested:
- Weather/PV conditions: low / medium / high solar
- Dynamic pricing used: yes / no

Do **not** include addresses, private IPs, serial numbers, account IDs, tokens or screenshots containing personal data.

## Scenario checks

### Idle / low household load

- Expected behaviour:
- Observed behaviour:
- Unexpected grid import/export:
- Result: pass / needs work

### High household load

- Expected behaviour:
- Observed behaviour:
- Peak grid import:
- Result: pass / needs work

### Solar surplus

- Expected behaviour:
- Observed behaviour:
- Did both battery systems avoid working against each other?
- Result: pass / needs work

### Battery near minimum SoC

- Expected behaviour:
- Observed behaviour:
- Safety limit respected:
- Result: pass / needs work

### Battery near maximum SoC

- Expected behaviour:
- Observed behaviour:
- Safety limit respected:
- Result: pass / needs work

### Temporary telemetry failure

- Expected behaviour:
- Observed behaviour:
- Controller fallback:
- Result: pass / needs work

### Price/deadline planning

- Expected behaviour:
- Observed behaviour:
- Unnecessary grid charging observed:
- Result: pass / needs work

### SELL / export

- Mode: shadow / active
- Expected behaviour:
- Observed behaviour:
- Result: pass / needs work / not tested

## Summary

- Stable features:
- Preview features:
- Shadow-only features:
- Problems found:
- Changes made after the test:
- Ready for public release: yes / no

## Publication rule

Only publish results that were actually observed. Do not label a scenario as tested when it was not reached during the test window.
