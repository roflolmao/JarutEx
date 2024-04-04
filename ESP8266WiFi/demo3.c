#include <ESP8266WiFi.h>

void setup() {
  Serial.begin(115200);
  Serial.println("\n\r---------------------\n\r");
  WiFi.mode(WIFI_STA);
  bool wpsStatus = WiFi.beginWPSConfig();
  if (wpsStatus) {
    Serial.println("WPS success.");
    while (WiFi.status() != WL_CONNECTED) {
      delay(330);
    }
    Serial.print("IP Address : ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("WPS failed!!!");
  }
}

void loop() {
}
