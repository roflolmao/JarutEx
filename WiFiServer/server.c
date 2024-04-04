//  2-Server
// WIFI_STA
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#define AP_NAME "JarutEx"
#define AP_PASSWD "123456789"

ESP8266WiFiMulti  wifiMulti;
WiFiServer server(3003);
IPAddress ip(192, 168, 1, 100);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);

void setup() {
  Serial.begin(115200);
  Serial.println("\n\r\n\r");
  WiFi.mode( WIFI_STA );
  wifiMulti.addAP( AP_NAME, AP_PASSWD );
  while (wifiMulti.run() != WL_CONNECTED) {
    delay(500);
  }
  Serial.println(WiFi.localIP());
  server.begin();
  Serial.println("Server begin.");
  Serial.print("Status: "); Serial.println(WiFi.status());  
  Serial.print("IP: ");     Serial.println(WiFi.localIP());
  Serial.print("Subnet: "); Serial.println(WiFi.subnetMask());
  Serial.print("Gateway: "); Serial.println(WiFi.gatewayIP());
  Serial.print("SSID: "); Serial.println(WiFi.SSID());
  Serial.print("Signal: "); Serial.println(WiFi.RSSI());
  Serial.print("Networks: "); Serial.println(WiFi.scanNetworks());
}

void loop() {
  if (wifiMulti.run() == WL_CONNECTED) {
    WiFiClient client = server.available();
    if (client) {
      if (client.connected()) {
        String req = client.readStringUntil('\r');
        Serial.print("From client:");
        Serial.println(req);
        client.flush();
        client.println(req);
        client.stop();
      } else {
        delay(5000);
        Serial.print("+");
      }
    }
  }
}
