#include <ESP8266WiFi.h>

IPAddress myIP(192, 168, 4, 54);
IPAddress gwIP(192, 168, 4, 11);
IPAddress subnet(255, 255, 255, 0);
uint8_t myMACaddr[6] = {99, 99, 99, 99, 99, 99};

void setup() {
  Serial.begin(115200);
  Serial.println("\n\r\n\r");
  WiFi.softAPmacAddress( myMACaddr );
  Serial.print("MAC Address : ");
  Serial.println(WiFi.softAPmacAddress());
  Serial.printf("%d:%d:%d:%d\n\n",
                myMACaddr[0],
                myMACaddr[1],
                myMACaddr[2],
                myMACaddr[3],
                myMACaddr[4],
                myMACaddr[5]);
  if (WiFi.softAPConfig( myIP, gwIP, subnet )) {
    if (WiFi.softAP("JarutEx", "123456789", 8, true, 3)) {
      Serial.print("IP Address : ");
      Serial.println(WiFi.softAPIP());
      Serial.print(WiFi.softAPgetStationNum());
      Serial.println(" connected.");
      WiFi.softAPdisconnect();
    } else {
      Serial.println("softAP() failed!!");
    }
  } else {
    Serial.println("softAPConfig() failed!");
  }
}

void loop() {
}
