// Node 1 : SoftAP
#include <ESP8266WiFi.h>

IPAddress myIP(192, 168, 4, 1);
IPAddress gwIP(192, 168, 4, 10);
IPAddress subnet(255, 255, 255, 0);

#define SSID "JarutEx"
#define PSK "123456789"

void setup() {
  Serial.begin(115200);
  Serial.println("\n\r\n\r");
  Serial.print("MAC Address : ");
  Serial.println(WiFi.softAPmacAddress());
  if (WiFi.softAPConfig( myIP, gwIP, subnet )) {
    if (WiFi.softAP(SSID, PSK, 8, true, 3)) {
      Serial.print("IP Address : ");
      Serial.println(WiFi.softAPIP());
      Serial.print(WiFi.softAPgetStationNum());
      Serial.println(" connected.");
      // WiFi.softAPdisconnect();
    } else {
      Serial.println("softAP() failed!!");
    }
  } else {
    Serial.println("softAPConfig() failed!");
  }
}

void loop() {
}
