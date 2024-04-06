#include <SoftwareSerial.h>

#define PIN_LED PA4
SoftwareSerial mySerial(PA10, PA9); // RX, TX

void setup() {
  mySerial.begin(9600);
  pinMode( PIN_LED, OUTPUT );
}

void loop() {
  mySerial.println("hi");
  digitalWrite( PIN_LED, HIGH );
  delay(500);
  digitalWrite( PIN_LED, LOW );
  delay(500);
}
