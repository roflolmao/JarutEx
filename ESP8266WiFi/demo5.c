#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

ESP8266WiFiMulti  wifiMulti;

void doConnect() {
  if (wifiMulti.run() != WL_CONNECTED) {
    delay(500);
  } 
  else  {
    Serial.printf("SSID : %s\n", WiFi.SSID());

    Serial.print("Hostname :");
    Serial.println(WiFi.hostname());
    Serial.print("\nMAC Address:  ");
    Serial.println(WiFi.macAddress());
    Serial.print("IP Address :");
    Serial.println(WiFi.localIP());
    Serial.print("subnetmask :");
    Serial.println(WiFi.subnetMask());
    Serial.print("Gateway :");
    Serial.println(WiFi.gatewayIP());
    Serial.print("DNS:");
    Serial.print(WiFi.dnsIP(0));
    Serial.print(", ");
    Serial.println(WiFi.dnsIP(1));
    Serial.print("SSID :");
    Serial.print(WiFi.SSID());
    Serial.print(" PSK:");
    Serial.println(WiFi.psk());
    Serial.printf("BBSD: %s\n",WiFi.BSSIDstr().c_str());
    Serial.printf("RSSI: %s dBm\n", WiFi.RSSI());
    Serial.println();
    WiFi.printDiag(Serial);
  }
}

void setup() {
  Serial.begin(115200);
  Serial.println("\n\n");
  wifiMulti.addAP( "SSID1", "PASSWD1" );
  wifiMulti.addAP( "SSID2", "PASSWD2" );
  wifiMulti.addAP( "SSID3", "PASSWD3" );
  wifiMulti.addAP( "SSID4", "PASSWD4" );
  wifiMulti.addAP( "SSID5", "PASSWD5" );
}

void loop() {
  doConnect();
  delay(5000);
}
