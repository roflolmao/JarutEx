#include <DHT.h>

DHT dht = DHT(D2, DHT11);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float tc = dht.readTemperature();
  float tf = dht.readTemperature(true);

  if (isnan(h) || isnan(tc) || isnan(tf)) {
    Serial.println("DHTsensor Failed");
    return;
  }

  float hic = dht.computeHeatIndex(tc, h, false);
  float hif = dht.computeHeatIndex(tf, h);

  Serial.println("--------------------------------");
  Serial.print("Temperature ...:");
  Serial.print(tc);
  Serial.print("C/");
  Serial.print(tf);
  Serial.println("F");
  Serial.print("Heat index ....:");
  Serial.print(hic);
  Serial.print("C/");
  Serial.print(hif);
  Serial.println("F");
  Serial.print("Humidity ......:");
  Serial.print(h);
  Serial.println("%");

  delay(1000);
}
