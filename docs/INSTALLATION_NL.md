# Installatiehandleiding (Nederlands)

## Aanbevolen: installeren via HACS Custom Repository

### 1. Maak een Home Assistant-back-up

Maak vóór het installeren van een custom integration altijd eerst een actuele Home Assistant-back-up.

### 2. Voeg de repository toe aan HACS

Ga in HACS naar **Custom repositories** en voeg deze repository toe:

`https://github.com/drosharold-coder/mova-lumegret-home-assistant`

Kies als categorie **Integration**.

### 3. Installeer MOVA LumeGret Energy

1. Zoek in HACS naar **MOVA LumeGret Energy**.
2. Installeer de nieuwste release.
3. Herstart Home Assistant.

### 4. Voeg de integratie toe

1. Ga naar **Instellingen -> Apparaten & diensten**.
2. Kies **Integratie toevoegen**.
3. Zoek op **MOVA LumeGret Energy**.
4. Log in met hetzelfde MOVAhome EU-account dat in de officiële MOVAhome-app werkt.
5. Rond de configuratie af.

### 5. Controleer apparaten en entiteiten

Bij de geteste opstelling horen onder andere zichtbaar te worden:

- MOVA LumeGret A4000;
- MOVA Smart Meter P1;
- batterijstatus en batterijvermogen;
- laden/ontladen;
- netvermogen, afname en teruglevering.

De B4000-uitbreiding maakt deel uit van de geteste accusamenstelling, maar verschijnt in deze integratie niet als apart cloudapparaat.

## Bijwerken via HACS

1. Open HACS.
2. Controleer op updates.
3. Werk **MOVA LumeGret Energy** bij.
4. Herstart Home Assistant.
5. Controleer daarna het versienummer op de integratiepagina.

## Handmatige installatie

Kopieer de map `custom_components/mova_lumegret` naar:

```text
/config/custom_components/mova_lumegret/
```

Herstart Home Assistant en voeg daarna de integratie toe via **Instellingen -> Apparaten & diensten**.

## Energy Dashboard

Zie `docs/DASHBOARD.md` en `optional/mova_energy_dashboard.yaml` voor de optionele batterij-energiesensoren.

## Privacy

Deel nooit wachtwoorden, tokens, cookies, `.storage`-bestanden, adressen, privé-IP-adressen of persoonlijke apparaat-ID's op GitHub.

Werkt iets niet, kijk dan eerst in `TROUBLESHOOTING.md`.
