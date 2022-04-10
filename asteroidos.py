https://ctrlv.sk/xjTd naprazdno
https://ctrlv.sk/kUCx nakratko
cloud6c.edupage.org/cloud/Elektrotechnicke_meranie_I_-_teoria_1_.pdf?z%3A0ZNOLkzLAhrrkTD1mvIqlV5%2BZ2p%2F%2BxFzRFE%2FztOZVnWj1CpnmjFOM%2BzuIXU7AahL




#include <Wire.h>
#include <BH1750.h>
#include <ThingSpeak.h>
#include <WiFi.h>

#define CHANNEL_ID 1700165
#define CHANNEL_API_KEY "L12O13TMH8QKSI62"

WiFiClient client;

#define WIFI_TIMEOUT_MS 20000
#define WIFI_NETWORK "Xiaomi_VJ"
#define WIFI_PASSWORD "cobrajez432"

void connectToWiFi(){
  Serial.print("Connecting to Wifi");
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_NETWORK, WIFI_PASSWORD);

  unsigned long startAttemptTime = millis();

  while (WiFi.status() != WL_CONNECTED &&
           millis()- startAttemptTime < WIFI_TIMEOUT_MS){
    Serial.print(".");
    delay(100);
           }
   if(WiFi.status() != WL_CONNECTED){
    Serial.println("Failed!");
   }else{
    Serial.print("Connected!");
    Serial.println(WiFi.localIP());
   }
}

BH1750 lightMeter(0x23);

void setup() {
  Serial.begin(115200);
  connectToWiFi();
  Wire.begin();
  lightMeter.begin();
  ThingSpeak.begin(client);
}

void loop() {
  
  uint16_t lux = lightMeter.readLightLevel();
  ThingSpeak.writeField(CHANNEL_ID, 1, lux, CHANNEL_API_KEY);
  Serial.print("Light: ");
  Serial.print(lux);
  Serial.println(" lx");
  delay(15000);
}
