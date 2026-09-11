# Installation guide

## Recommended: HACS custom repository

### 1. Create a Home Assistant backup

Before installing any custom integration, create a current Home Assistant backup.

### 2. Add the repository to HACS

In HACS:

1. Open **HACS**.
2. Open the menu and choose **Custom repositories**.
3. Add:

   `https://github.com/drosharold-coder/mova-lumegret-home-assistant`

4. Select category **Integration**.
5. Confirm/add the repository.

### 3. Install MOVA LumeGret Energy

1. Find **MOVA LumeGret Energy** in HACS.
2. Install the latest release.
3. Restart Home Assistant when prompted, or restart manually.

### 4. Add the integration

1. Open **Settings -> Devices & services**.
2. Select **Add integration**.
3. Search for **MOVA LumeGret Energy**.
4. Enter the same MOVAhome EU account credentials that work in the official MOVAhome app.
5. Complete setup.

### 5. Verify devices and entities

For the verified setup you should see:

- MOVA LumeGret A4000;
- MOVA Smart Meter P1;
- A4000 battery telemetry;
- P1 grid import/export telemetry.

The B4000 expansion is part of the tested battery stack but is not currently exposed as a separate cloud device.

## Updating through HACS

1. Open HACS.
2. Check for updates.
3. Update MOVA LumeGret Energy.
4. Restart Home Assistant.
5. Verify the integration version on the integration page.

If HACS still shows an old version, refresh HACS information and verify that the repository URL points to `drosharold-coder/mova-lumegret-home-assistant`.

## Manual installation

1. Download the release archive from GitHub.
2. Copy `custom_components/mova_lumegret` to:

```text
/config/custom_components/mova_lumegret/
```

3. Restart Home Assistant.
4. Add **MOVA LumeGret Energy** from **Settings -> Devices & services**.

## Optional Energy Dashboard support

See `docs/DASHBOARD.md` and `optional/mova_energy_dashboard.yaml`.

## Security/privacy

Do not publish:

- MOVAhome passwords;
- access/refresh tokens;
- cookies;
- Home Assistant `.storage` files;
- home addresses;
- private IP addresses;
- unique personal device identifiers.

If something fails, see `TROUBLESHOOTING.md` before opening an issue.
