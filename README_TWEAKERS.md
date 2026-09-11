# MOVA LumeGret A4000 + Smart Meter P1 werkend in Home Assistant

Ik heb de MOVA LumeGret A4000, in mijn testopstelling samen met een B4000-uitbreiding, gekoppeld aan Home Assistant via een eigen community custom integration.

GitHub:
https://github.com/drosharold-coder/mova-lumegret-home-assistant

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

Handmatig installeren kan ook door `custom_components/mova_lumegret` naar `/config/custom_components/mova_lumegret` te kopiëren.

## Meerdere merken thuisaccu's in dezelfde Home Assistant-opstelling

De MOVA kan ook onderdeel zijn van een Home Assistant-opstelling waarin een thuisaccu van een ander merk aanwezig is. Home Assistant kan de telemetrie van beide systemen naast elkaar gebruiken voor dashboards, historie en energiemanagement.

Belangrijk: dit betekent niet dat MOVA officieel rechtstreeks met een specifiek ander merk koppelt. De samenwerking gebeurt op Home Assistant-/EMS-niveau. Deze publieke MOVA-integratie blijft bewust read-only.

Als beide accusystemen daarnaast via betrouwbare schrijfbare integraties of fabrikant-API's aangestuurd kunnen worden, kan een aparte EMS-regellaag bepalen welke accu wanneer mag laden of ontladen. Dat voorkomt dat twee zelfstandige regelingen elkaar gaan tegenwerken.

De uitgebreide uitleg, inclusief architectuurschema, conflictpreventie en testchecklist, staat hier:
`docs/MULTI_BATTERY_NL.md`

## Extra documentatie

De GitHub-repository bevat inmiddels ook:

- Nederlandse en Engelse installatiehandleiding;
- ondersteunde apparaten/model-ID's;
- troubleshooting en FAQ;
- architectuuroverzicht;
- uitleg voor multi-brand thuisaccu-opstellingen;
- testmatrix/releasechecklist;
- dashboard- en Energy Dashboard-uitleg;
- roadmap en contribution guide;
- issue-templates voor bugs en ondersteuning van andere MOVA-modellen.

Er zit ook een optioneel YAML-package bij voor cumulatieve laad-/ontlaadenergie in het Home Assistant Energy Dashboard.

## Belangrijk

Dit is een **onofficiële community-integratie** en geen officiële MOVA- of Home Assistant-koppeling. De cloudinterface kan wijzigen. De publieke GitHub-versie bevat bewust geen experimentele schrijf-/EMS-code en geen persoonlijke tokens of device-ID's.

Ik hoor graag praktijkervaringen van andere A4000/P1-gebruikers. Voor andere MOVA-energiemodellen kan via GitHub een device-support issue worden geopend zonder privégegevens te delen.

Huidige publieke release: **v0.1.3**

Volgende release in voorbereiding: **v0.1.4**
