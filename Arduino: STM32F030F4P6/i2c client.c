////////////////////////////////////////////////////////////////////////
// i2c client
// STM32F030F4P6
// Address 0x17
// Input
//     Byte 1
//        0 Blink LED : PA4
// (C) 2021, JarutEx
////////////////////////////////////////////////////////////////////////
#include <Wire.h>
int unoAddr = 0x17;
#define ledPin PA4

void i2cReceive( int bytes ) {
  uint8_t dInput = Wire.read(); // command
  uint8_t dValue = Wire.read(); // argument
  if (dInput == 0) { // Flash
    if (dValue == 0) {
      digitalWrite(ledPin, HIGH);
    } else if (dValue == 1) {
      digitalWrite(ledPin, LOW);
    }
  }
}
void i2cRequest() {
  Wire.write(0x00);
}
void setup() {
  pinMode( ledPin, OUTPUT );
  digitalWrite( ledPin, HIGH); // off LED
   Wire.begin(unoAddr);
  Wire.onReceive(i2cReceive);
  Wire.onRequest(i2cRequest);
}
void loop() {
}
