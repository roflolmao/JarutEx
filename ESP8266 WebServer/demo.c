#include <DHT.h>

DHT dht = DHT(5, DHT11); // D1
float minC = 100.0f, maxC = 0.0f; // อุณหภูมิต่ำสุด/สูงสุด
float minH = 100.0f, maxH = 0.0f; // ความชื้นต่ำสุด/สูงสุด
void setup() {
  Serial.begin(115200);
  Serial.println("\n\n\n");
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float tc = dht.readTemperature();
  float tf = dht.readTemperature(true);

  if (isnan(h) || isnan(tc) || isnan(tf)) {
    Serial.println("DHT11 connect failed!");
    return;
  }

  float hic = dht.computeHeatIndex(tc, h, false);
  float hif = dht.computeHeatIndex(tf, h);

  if (minC > tc) {
    minC = tc;
  }
  if (maxC < tc) {
    maxC = tc;
  }
  if (minH > h) {
    minH = h;
  }
  if (maxH < h) {
    maxH = h;
  }

  Serial.printf("Temperature: %.2fC/%.2fF Huminitt: %.2f%%, Heat index: %.2fC/%.2fF\n",
                tc, tf, h, hic, hif);
  Serial.printf("Temp. (%.2fC-%.2fC) Hum. (%.2f%%-%.2f%%)\n",
                minC, maxC, minH, maxH);
  delay(10000);
}
