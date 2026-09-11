"""Constants for MOVA LumeGret Energy."""
DOMAIN = "mova_lumegret"
PLATFORMS = ["sensor"]
CONF_EMAIL = "email"
DEFAULT_SCAN_INTERVAL = 10
MODEL_A4000 = "mova.bkw.ge2505"
MODEL_P1 = "mova.sme.ge2608"
STATUS_MAP = {
    0: "Power Off",
    1: "Standby",
    2: "Off Grid",
    3: "Grid Tied",
    4: "Fault",
    5: "Grid-tied operation",
    6: "Running off-grid with load",
}
