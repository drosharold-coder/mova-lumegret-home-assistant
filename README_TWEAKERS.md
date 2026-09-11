# MOVA LumeGret A4000 + Smart Meter P1 werkend in Home Assistant

Ik heb de MOVA LumeGret A4000, in mijn testopstelling samen met een B4000-uitbreiding, gekoppeld aan Home Assistant via een eigen community custom integration.

De versie die ik publiek deel is bewust **read-only**. Home Assistant leest de accu en de MOVA Smart Meter P1 uit, maar stuurt vanuit deze publieke integratie geen laad-, ontlaad- of andere besturingscommando's naar de batterij.

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

## Installatie

De GitHub-repository is opgebouwd als normale Home Assistant custom integration en is voorbereid om ook als HACS custom repository te gebruiken.

Handmatig kan het ook:

1. Maak een Home Assistant-back-up.
2. Kopieer `custom_components/mova_lumegret` naar `/config/custom_components/mova_lumegret`.
3. Herstart Home Assistant.
4. Ga naar **Instellingen -> Apparaten & diensten -> Integratie toevoegen**.
5. Zoek op **MOVA LumeGret Energy**.
6. Log in met je MOVAhome-account.

Er zit ook een optioneel YAML-package bij voor cumulatieve laad-/ontlaadenergie in het Home Assistant Energy Dashboard.

## Belangrijk

Dit is een **onofficiële community-integratie** en geen officiële MOVA- of Home Assistant-koppeling. De cloudinterface kan wijzigen. De publieke GitHub-versie bevat bewust geen experimentele schrijf-/EMS-code en geen persoonlijke tokens of device-ID's.

Versie: **v0.1.3**
