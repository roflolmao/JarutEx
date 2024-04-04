#include <ESP8266WiFi.h>

void showAPs( int networksFound ) {
  Serial.printf("Found %d AP(s)\n", networksFound);
  for (int i = 0; i < networksFound; i++)  {
    Serial.print("AP No.");
    Serial.print(i + 1);
    Serial.print(" : ");
    Serial.print(WiFi.SSID(i));
    if (WiFi.isHidden( i )) {
      Serial.print("*");
    }
    Serial.print(" Ch:");
    Serial.print(WiFi.channel(i));
    Serial.print(" S:");
    Serial.print(WiFi.RSSI(i));
    Serial.print("dBm ENC:");
    switch (WiFi.encryptionType(i)) {
      case ENC_TYPE_TKIP:
        Serial.print("WPA/PSK");
        break;
      case ENC_TYPE_CCMP:
        Serial.print("WPA2/PSK");
        break;
      case ENC_TYPE_WEP:
        Serial.print("WEP");
        break;
      case ENC_TYPE_NONE:
        Serial.print("Open");
        break;
      case ENC_TYPE_AUTO:
        Serial.print("WPA/WPA2/PSK");
        break;
      default:
        Serial.print("Unknown");
    }
    Serial.print(" BSSID:");
    Serial.println(WiFi.BSSIDstr(i));
  }
}

void setup() {
  Serial.begin(115200);
  Serial.println("\n\r\n\r");
  WiFi.mode( WIFI_STA );
  WiFi.disconnect();
  delay(100);
  WiFi.scanNetworksAsync( showAPs, true );
}

void loop() {
}
