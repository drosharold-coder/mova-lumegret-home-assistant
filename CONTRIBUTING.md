# Contributing

Thanks for helping improve the MOVA LumeGret Home Assistant community integration.

## Principles

- Keep the public project read-only unless the project scope is explicitly changed in the future.
- Never commit MOVAhome passwords, access/refresh tokens, cookies, private LAN addresses, home addresses or personal device identifiers.
- Do not claim support for hardware that has not been tested on a real device/account.
- Prefer small, reviewable changes with clear descriptions.

## Reporting a bug

Please include:

- Home Assistant Core version;
- integration version;
- MOVA hardware model;
- whether the official MOVAhome app is working;
- expected behavior;
- actual behavior;
- sanitized relevant log lines.

Remove credentials, tokens, cookies, addresses and unique device identifiers before posting logs.

## Adding a device/model

Before implementing support, open an issue with the product name and non-sensitive information. A new model should only be marked supported after its model ID, telemetry properties, units/signs and cloud behavior have been verified.

## Pull requests

Before opening a PR:

1. Run/verify Python syntax.
2. Confirm `set_properties` or other battery-control writes have not been introduced accidentally.
3. Keep HACS validation green.
4. Keep Home Assistant Hassfest validation green.
5. Update documentation/changelog when user-visible behavior changes.

## Translations

Translations are welcome. Keep `translations/en.json` as the reference English translation and add locale files using Home Assistant conventions.

## Branding

Do not add an official MOVA/LumeGret logo unless explicit permission to use that asset in this open-source project has been obtained from MOVA.
