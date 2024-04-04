// Arduino Mega2560

#include <DHT.h>

DHT dht = DHT(13, DHT11);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {

  float h = dht.readHumidity();
  float tc = dht.readTemperature();
  float tf = dht.readTemperature(true);

  if (isnan(h) || isnan(tc) || isnan(tf)) {
    Serial.print("DHTsensor Failed");
    return;
  }

  float hic = dht.computeHeatIndex(tc, h, false);
  float hif = dht.computeHeatIndex(tf, h);

  Serial.print("T: ");
  Serial.print(tc);
  Serial.print("C/");
  Serial.print(tf);
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print("%, ");
  Serial.print("   Heat index   ");
  Serial.print(hic);
  Serial.print("C/");
  Serial.print(hif);
  Serial.println("F");
  delay(5000);
}
