#include <ESP8266WiFi.h>

#define AP_NAME "ชื่อ AP"
#define AP_PASSWD "รหัสผ่าน"

void setup() {
  Serial.begin(115200);
  Serial.println("\n\n");
  WiFi.begin( AP_NAME, AP_PASSWD );
  int countLimit = 200;
  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
    if (countLimit == 0) {
      break;
    }
    countLimit--;
  }
  if (countLimit > 0) {
    Serial.println(WiFi.localIP());
    WiFi.printDiag(Serial);
  }
  WiFi.disconnect();
}

void loop() {
}
