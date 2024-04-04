// 3-Client
// WIFI_STA
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#define AP_NAME  "JarutEx"
#define AP_PASSWD  "123456789"
ESP8266WiFiMulti  wifiMulti;
WiFiClient client;
IPAddress sIP(192, 168, 4, 100);

void setup() {
  Serial.begin(115200);
  Serial.println("\n\r\ns\r");
  WiFi.mode( WIFI_STA );
  wifiMulti.addAP( AP_NAME, AP_PASSWD );
  while (wifiMulti.run() != WL_CONNECTED) {
    delay(500);
  }
  Serial.println(WiFi.localIP());
  Serial.println("Client  begin.");
}

void loop() {
  if (wifiMulti.run() == WL_CONNECTED) {
    if (client.connect( sIP, 3003 )) {
      Serial.println("Connected.");
      client.println("Hello, World!\r");
      while (!client.available());
      String echoStr = client.readStringUntil('\r');
      client.flush();
      Serial.print("From server:");
      Serial.println(echoStr);
      client.stop();
      delay(10000);
    }
  } else {
    delay(5000);
  }
}
