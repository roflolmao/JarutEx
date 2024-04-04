#include <Wire.h>
int unoAddr = 7;
void i2cReceive( int bytes ) {
  uint8_t dInput = Wire.read();
  uint8_t pattern = Wire.read();
  Serial.println(dInput);
  if (dInput == 0) {
    for (int ledPin = 2; ledPin <= 9; ledPin++) {
      pinMode(ledPin, OUTPUT);
    }
    for (int ledPin = 2; ledPin <= 9; ledPin++) {
      digitalWrite(ledPin, 0);
    }
  }
  else if (dInput == 1) {
    for (int ledPin = 2; ledPin <= 9; ledPin++) {
      pinMode(ledPin, OUTPUT);
    }
    for (int ledPin = 2; ledPin <= 9; ledPin++) {
      digitalWrite(ledPin, 1);
    }
  }
  else if (dInput == 2) {
    for (int ledPin = 2; ledPin <= 9; ledPin++) {
      pinMode(ledPin, OUTPUT);
    }
    uint8_t mask = 0x01;
    for (int ledPin = 2; ledPin <= 9; ledPin++) {
      digitalWrite(ledPin, pattern & mask);
      mask <<= 1;
    }
  } else {
    return;
  }
}
void i2cRequest() {
  for (int ledPin = 2; ledPin <= 9; ledPin++) {
    pinMode(ledPin, INPUT_PULLUP);
  }
  uint8_t bitNo = 0;
  uint8_t unoBuffer = 0;
  for (int swPin = 2; swPin <= 9; swPin++) {
    unoBuffer |= digitalRead( swPin ) << bitNo;
    bitNo++;
  }
  Serial.println(unoBuffer, HEX);
  Wire.write(unoBuffer);
}
void setup() {
  Serial.begin(115200);
  Serial.println("UNO Started");
  Wire.begin(unoAddr);
  Wire.onReceive(i2cReceive);
  Wire.onRequest(i2cRequest);
}
void loop() {
}
