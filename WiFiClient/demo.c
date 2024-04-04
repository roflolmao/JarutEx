#include <ESP8266WiFi.h>
#include <WiFiClient.h>

#define AP_NAME "ชื่อAP"
#define AP_PASSWD "รหัสของAP"

WiFiClient client;

void setup() {
  Serial.begin(115200);
  Serial.println("\n\n");
  WiFi.mode(WIFI_STA);

  WiFi.begin( AP_NAME, AP_PASSWD );
  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
    Serial.print(".");
  }

  if (client.connect("jarutex.com", 80)) {
    Serial.println("Yes");
    client.print(String("GET ") + "/" + " HTTP/1.1\r\n" +
                 "Host: " + "jarutex.com" + "\r\n" +
                 "Connection: close\r\n\r\n");
    delay(1000);
    while (client.available()) {
      String line = client.readStringUntil('\r');
      Serial.print(line);
    }
    client.stop();
  } else {
    Serial.println("OMG!");
  }
  WiFi.disconnect();
}

void loop() {
}
