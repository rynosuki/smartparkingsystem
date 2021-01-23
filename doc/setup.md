**The Things Network**

Steg 1: Skapa en application genom att klicka på "application"
<img src="/img/ubidots1.jpg" width="800">

Steg 2: Skriv ett unikt id för applicationen exempelvis "bilsensor"
<img src="/img/ubidots2.jpg" width="800">

Steg 3: klicka sedan på register device

<img src="/img/ubidots3.jpg" width="800">


Steg 4: Skriv ett unikt deviceid sedan skriver du in ditt device eui som du får fram genom att
skriva
```python
print("DevEUI: " + ubinascii.hexlify(lora.mac()).decode('utf-8').upper())

```
Sedan kopierar du DeviceEUI och klistra in den på DeviceEUI på the things Network. Sedan klickar du på register.

Steg 5: Decode (Payload functions)
Skriv En payload function för att kunna skicka värden som du anpassar beroende beroende på hur mycket bytes man skickar.
```java
function Decoder(bytes, port) {
  var openslots = bytes[0];
  
  return {
     openslots: openslots
  }
}
```
**Ubidots**
Steg 1: Klicka på api credentials och sedan kopiera default token.
<img src="/img/ubidots5.jpg" width="800">

Steg 2 Sedan gå in på the things network på application>applicationname>integrations.Klicka sedan på add integrations och sedan på ubidots.
Klistra in ubidots token på token. Klicka sedan på save.

<img src="/img/ubidots6.jpg" width="800">

Steg 3: Skapa en ny dashboard genom att klicka på data sedan på dashboards och sedan på plustecknet för att lägga till widget som kan vara exempelvis en graf.
