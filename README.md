# Parkeringshjälpssystem för två system.

## Introduktion
Projektet bygger på ett system som ska hjälpa till att räkna antalet bilar som finns inne på en parkeringsyta. Detta har valts att göras via två separata system, där en fungerar för större parkeringsytor genom att räkna antalet bilar som kör in på området och hur många som kör ut. Det andra systemet är konstruerat för enskilda parkeringar, där man med en enhet kan mäta upp till 8 parkeringsfickor och få information om någon är parkerad där. 

## Redovisningsklipp

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/F4wCRsl9FjA/0.jpg)](https://www.youtube.com/watch?v=F4wCRsl9FjA)

## Bakgrund och idé
Parkeringshjälpsystemet var ett önskemål från Kalmar Kommun där man vill ha en produkt som skulle hjälpa till att hålla koll på antalet bilar som fanns på parkeringsytorna i Kalmar området och kunna visualisera datan för alla parkeringar i kalmar området. En möjlig uppgradering till det system som finns idag. 

Projektet byggdes från den information som tilldelats från Kalmar Kommun, en produkt med två system där man kan mäta antalet bilar i större parkeringsytor men även ett system för enskilda parkeringsytor som finns runt om i Kalmar. Denna informationen skulle kunna skickas upp till nätet för att visualiseras och bearbetas. 

Under projektet valdes TTN (The Things Network) och Ubidots som de verktyg som skulle användas för lagring av data och presentering. Detta gav en bra visualisering av den data som eftersöktes.

## Metod
Projektet valdes att delas upp i tre olika delmoment, en arbetade med in- och utpasseringssystemet och LoRa, en med visualisering och den sista med enskilda parkeringsfickor. Detta visade sig vara en optimal lösning eftersom det fanns många olika verktyg för visualisering och behövdes tid för att förstå hur man skulle gå väga. Uppkopplingen till LoRa tog en längre tid än vad som hade planerats för, detta p.g.a ett kopplingsfel i kretsen och för långt avstånd till en gateway. 

Arbetet valdes att göra helt på distans förutom en veckoträff på tre timmar i veckan där man kom ihop och pratade om hur man skulle gå vidare och även lösningar på problem som man stött på. Kommunikationen valdes istället att göras på discord istället för via GitLab, detta p.g.a att gruppen inte var insatta i hur Git fungerade tidigare. 

Innan projektet påbörjades så bestämdes en mängd krav som produkten skulle lösa, dessa hittas i [requirements.md](/doc/requirements.md).

Ytterliggare information angående uppkoppling, installation och test finns i dokumentationen nedan.

- [Hårdvaruinstallation](/doc/hardware.md)
- [Mjukvaruinstallation](/doc/setup.md)
- [Testning](/doc/test.md)

Struktering och kodning valdes att göras i programmet Atom, med tillägget pymakr. Detta rekommenderas vid testning av produkten för uppladdning av programmet. 

## Resultat
Produkten når upp till de mål som tidigare satts, med några felkällor som uppstod p.g.a val av sensor och tidsbegränsning. 

Man mäter om en bil kör in eller ut från parkering genom att kolla vilken sensor som aktiveras först, inom en bestämd tidsram. Detta gav möjliga problem om det är personer som vandrar samtidigt som någon kör förbi med en bil. Då skulle båda sensorer aktiveras samtidigt och bilen skulle inte räknas med, detta antas kunna lösas med en annan typ av sensor. 

### Visualisering av produkten
En huvudpunkt i produktenskrav är att ha möjligheten att se datan online för att få en överblick över hur parkeringsläget ser ut, detta visas genom en graf över de senaste 24 timmarna och men det går även att se grafen i vilket format som helst genom att klicka på "explore data".

<img src="/img/vis.jpg" width="800">
