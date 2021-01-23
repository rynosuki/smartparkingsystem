# Test av Parkeringshjälpsystem

## Tester gjorda av gruppen

Under projektets gång så har produkten kontinuerligt testats mot de krav som ställts. Detta har gjorts med fysiska test där man rört sig framför sensorerna för att se att rätt värden fås. Man har även gjort teoretiska tester med valda värden som skickats upp mot TTN för visualisering och test av payload funktioner. 

Produkten har testats genom att föra händerna framför sensorerna för att testa tidsskillnad och överse hur produkten fungerar i verkligheten. Detta visade på ett par felkällor som tidigare missats, bestämning av tid från det att första sensorn aktiveras till nästa, vad händer om någon går förbi samtidigt, möjlighet för någon sorts threading. En annan stor felkälla visade sig vara sensorerna som användes, dessa var nästanintill omöjliga att arbeta med i detta syftet. 

En video där hela produkten för in- och utpasseringsystemet testas:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/30_rPo1NZzc/0.jpg)](https://www.youtube.com/watch?v=30_rPo1NZzc)


## In- och utgångssystem

1. Koppla upp kretsen med hjälp av informationen i [hardware.md](hardware.md)
2. (Om online funktionen önskas vid test) Sätt upp TTN och Ubidots enligt informationen i [setup.md](setup.md)
3. Ändra följande kod i main.py - där xx är koden ni får från TTN. Raderna 36 och 37.
```python
app_eui = ubinascii.unhexlify("xx")
app_key = ubinascii.unhexlify("xx")
```
4.
Ändra även följande del till "3" i rad 53.
```python
dev_type = 1
```
5. Ladda upp programmet till PyCom enheten.
6. Rör ett objekt mellan de två sensorerna där de båda är aktiverade med en tidskillnad på 1-2 sekunder. (Detta skickar information om att datan har ändrats i loggen)
7. (Online) Varje 60 sekund så skickas datan upp till TTN och Ubidots där ni kan se visualiseringen av hur många som är parkerade.

## System för enskilda parkeringar

Systemet ska fungera så att man har en sensor för varje enskild parkeringsplats, upp till 8 sensorer per enhet. Sedan ska programmet kunna se vilken sensor som är aktiv (alltså vilken parkering som är upptagen), samt räkna hur länge bilen stått parkerad. När bilen inte längre är parkerad sätter vi räknaren för tiden för sensorn tillbaka till noll. Varje minut skickas datan över alla sensorer för enheten, om det är en bil som är parkerad eller inte, samt tiden som den har varit parkerad isåfall.

Koden testades först genom att ändra intervallen då datan skickades, från 60 sekunder till 1 sekund. Då kunde vi få ständig data för att enklare se om koden fungerade. Vi höll en hand över sensorerna för att aktivera dem, och kunde genom datan som skickades se att det fungerade som det skulle. Sedan ändrade vi tillbaka intervallet till 60 sekunder, och det fungerade även då som det skulle.
