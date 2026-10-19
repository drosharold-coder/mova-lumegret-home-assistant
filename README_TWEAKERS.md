# MOVA LumeGret A4000 + Smart Meter P1 in Home Assistant

Ik heb de MOVA LumeGret A4000, in mijn testopstelling samen met een B4000-uitbreiding, gekoppeld aan Home Assistant via een eigen community custom integration.

MOVA heeft toestemming gegeven om het officiële MOVA/LumeGret-logo te gebruiken voor deze community Home Assistant-integratie op GitHub en HACS. De integratie zelf blijft onofficieel en community-onderhouden.

GitHub:
https://github.com/drosharold-coder/mova-lumegret-home-assistant

De publieke integratie is bewust **read-only**. Home Assistant leest de accu en MOVA Smart Meter P1 uit, maar stuurt vanuit deze integratie geen laad-, ontlaad- of andere besturingscommando's naar de batterij.

## Wat wordt uitgelezen?

**A4000**
- SoC
- batterijvermogen
- laadvermogen
- ontlaadvermogen
- batterijstroom
- richting
- bedrijfsstatus

**Smart Meter P1**
- netvermogen
- netafname
- teruglevering

De koppeling gebruikt de MOVAhome EU-cloud en leest standaard ongeveer iedere 10 seconden uit.

## Project inmiddels breder dan alleen uitlezen

Het project is inmiddels doorgegroeid naar een apart Home Assistant EMS waarin MOVA samen met een tweede batterijplatform in dagelijks gebruik wordt gecoördineerd.

De primaire praktijktest gebruikt **19,52 kWh totale nominale opslagcapaciteit** en omvat onder andere:

- zonne-overschot;
- HOUSE / bijna-nul-netregeling;
- SoC- en reservebeheer;
- high-load gedrag;
- failover en herstel;
- prijsbewust laden;
- multi-battery coördinatie.

Belangrijk: deze EMS-regeling staat **los van de publieke read-only MOVA-integratie**.

Een echte batterij-/netwerkuitval is inmiddels gebruikt om failover en herstel in de praktijk te testen.

Daarnaast wordt een tweede community-testopstelling in Frankrijk voorbereid met meerdere A4000-units en B4000-uitbreiding. Daarmee kunnen we later gedrag op een tweede woning valideren.

## Nieuwe community-vraag: PV1–PV4

Er is inmiddels ook een feature request voor read-only PV1–PV4 ingangsvermogens en totaal PV-vermogen van de A4000. Dat zit nog niet in v0.1.3 en wordt pas toegevoegd nadat de juiste properties op echte hardware zijn gevalideerd.

## Installeren via HACS

1. Open HACS.
2. Kies **Custom repositories**.
3. Voeg `https://github.com/drosharold-coder/mova-lumegret-home-assistant` toe.
4. Kies categorie **Integration**.
5. Installeer **MOVA LumeGret Energy**.
6. Herstart Home Assistant.
7. Ga naar **Instellingen -> Apparaten & diensten -> Integratie toevoegen**.
8. Zoek op **MOVA LumeGret Energy**.
9. Log in met hetzelfde MOVAhome-account als in de officiële app.

## Belangrijk

Dit is een **onofficiële community-integratie** en geen officiële MOVA- of Home Assistant-koppeling. De publieke GitHub-versie bevat bewust geen experimentele schrijf-/EMS-code en geen persoonlijke tokens, IP-adressen of device-ID's.

Huidige publieke release: **v0.1.3**

Volgende release in voorbereiding: **v0.1.4**, pas na de praktische HACS/update-test.
