# Meerdere merken thuisaccu's combineren met Home Assistant

Deze MOVA-integratie kan één onderdeel zijn van een Home Assistant-installatie waarin ook een thuisaccu van een ander merk aanwezig is.

Belangrijk: dit betekent **niet** dat MOVA officieel een ander accumerk ondersteunt of dat beide accu's rechtstreeks met elkaar koppelen. De systemen kunnen naast elkaar in dezelfde Home Assistant-omgeving worden gebruikt. Home Assistant kan de gegevens samenbrengen en kan — als voor beide systemen aparte schrijfbare integraties of API's beschikbaar zijn — ook als hogere regielaag dienen.

## Wat deze publieke MOVA-integratie ondersteunt

De MOVA LumeGret-integratie in deze repository is bewust **read-only**.

Zij levert Home Assistant telemetrie uit de geteste MOVA-opstelling, waaronder:

- laadstatus (SoC)
- batterijvermogen
- laad- en ontlaadvermogen
- batterijstroom
- richting / bedrijfsstatus
- Smart Meter P1 netafname en teruglevering

Home Assistant kan deze informatie naast gegevens van een ander thuisaccumerk tonen in dashboards, geschiedenis, statistieken en automatiseringen.

## Wat hiermee niet wordt beweerd

Deze documentatie beweert niet dat:

- MOVA officieel een specifiek ander accumerk ondersteunt;
- MOVA en een andere thuisaccu rechtstreeks met elkaar communiceren;
- deze publieke integratie laden of ontladen aanstuurt;
- iedere combinatie van twee accusystemen automatisch veilig of conflictvrij werkt;
- een specifiek ander accutype getest is, tenzij dat uitdrukkelijk als getest staat vermeld.

## Aanbevolen architectuur

```mermaid
flowchart LR
    Grid[Net / huishoudelijk vermogen] --> Meter[Net- / P1-meting]
    Meter --> HA[Home Assistant]
    MOVA[MOVA A4000 / accustack] -->|read-only telemetrie| HA
    Other[Thuisaccu ander merk] -->|telemetrie| HA
    HA --> Dash[Dashboards / historie / energiestatistieken]
    HA -. optionele aparte EMS-/regielaag .-> Control[Schrijfbare integraties / fabrikant-API's]
    Control -. indien ondersteund .-> MOVA
    Control -. indien ondersteund .-> Other
```

De publieke MOVA-integratie blijft aan de uitleeskant van dit schema. Schrijfcommando's en experimentele EMS-regeling horen bewust niet in deze publieke repository.

## Waarom centrale regie belangrijk is

Twee thuisaccu's die ieder zelfstandig op hetzelfde netvermogen reageren, kunnen elkaar tegenwerken. Bijvoorbeeld:

- de ene accu gaat laden terwijl de andere ontlaadt;
- beide reageren tegelijk op dezelfde netafname of teruglevering;
- twee verschillende regelingen blijven elkaar voortdurend corrigeren.

Daarom moet een multi-battery-opstelling één duidelijke regelstrategie hebben. In de praktijk zijn er drie logische modellen:

1. **Alleen monitoren** — beide accu's houden hun eigen fabrikantregeling en Home Assistant leest alleen mee.
2. **Prioriteitsregeling** — één accu is primair en de tweede mag alleen onder vooraf bepaalde voorwaarden reageren.
3. **Centrale EMS-regeling** — een aparte Home Assistant-/EMS-laag bepaalt welke accu wanneer mag laden of ontladen.

Voor optie 3 zijn betrouwbare schrijfbare interfaces nodig voor de betrokken accu's. Dat valt bewust buiten deze publieke read-only MOVA-integratie.

## Praktische ontwerpregels

Voor een stabiele opstelling met meerdere merken:

- gebruik waar mogelijk één consistente bron voor netvermogen;
- bepaal per beslissing welke regeling de baas is;
- voorkom dat twee zelfstandige zero-export- of zelfverbruikregelingen op hetzelfde meetsignaal reageren;
- werk met duidelijke laad- en ontlaadprioriteiten;
- stel per accu minimale en maximale SoC-grenzen in;
- gebruik hysterese / een dode band om snel heen-en-weer schakelen te voorkomen;
- zorg voor een veilige terugval als Home Assistant, netwerk of cloudverbinding wegvalt;
- respecteer de elektrische, thermische en garantievoorwaarden van iedere fabrikant;
- laat netaansluiting, beveiligingen en bekabeling waar nodig door een bevoegde installateur ontwerpen of controleren.

## Voorbeeld

Een woning kan bijvoorbeeld hebben:

- een MOVA LumeGret A4000 met B4000-uitbreiding;
- een MOVA Smart Meter P1;
- een tweede thuisaccu van een ander merk;
- Home Assistant als gezamenlijke monitoring- en energiemanagementlaag.

Home Assistant kan beide systemen dan in één overzicht tonen. Als beide accusystemen daarnaast over geschikte schrijfbare integraties beschikken, kan een aparte EMS-regeling ze coördineren zodat ze niet tegen elkaar in werken.

Nogmaals: deze merkoverstijgende samenwerking is een **Home Assistant-/EMS-oplossing**, geen officieel MOVA-naar-ander-merk protocol.

## Wanneer mag een combinatie "getest" worden genoemd?

Een specifieke combinatie zou pas als getest moeten worden vermeld nadat minimaal is gecontroleerd dat:

- beide systemen stabiele telemetrie leveren;
- netafname en teruglevering de juiste richting en schaal hebben;
- laden van accu 1 niet onbedoeld ontladen van accu 2 veroorzaakt;
- ontladen van accu 1 niet onbedoeld laden van accu 2 veroorzaakt;
- ingestelde SoC-grenzen worden gerespecteerd;
- gedrag na een Home Assistant-herstart voorspelbaar is;
- gedrag bij internet-, cloud- of API-uitval veilig blijft;
- na herstel van communicatie weer een bekende toestand ontstaat.

Zolang deze checks niet voor een specifiek tweede accutype zijn uitgevoerd, is de juiste formulering: **multi-brand mogelijk via Home Assistant-architectuur**, niet: officieel door MOVA compatibel verklaard.

## Grens van het publieke project

Deze repository houdt de MOVA-integratie zelf read-only. Conceptuele uitleg over meerdere accu's mag wel in de documentatie staan, maar experimentele schrijfcommando's, privé-reverse-engineeringgegevens, inloggegevens en persoonlijke device-ID's horen niet in de publieke integratie.