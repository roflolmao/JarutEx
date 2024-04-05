// code3-9 โค้ดของ Arduino Uno
#include <Wire.h>
int unoAddr = 7;
uint8_t ledStatus[8] = {1, 1, 1, 1, 1, 1, 1, 1};
void i2cReceive( int bytes ) {
  uint8_t dInput = Wire.read();
  uint8_t pattern = Wire.read();
  Serial.println(dInput);
  if (dInput == 0) {
    for (int ledPin = 2; ledPin <= 9; ledPin++) {
      digitalWrite(ledPin, 0);
      ledStatus[ledPin-2] = 0;
    }
  }
  else if (dInput == 1) {
    for (int ledPin = 2; ledPin <= 9; ledPin++) {
      digitalWrite(ledPin, 1);
      ledStatus[ledPin-1] = 1;
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
  for (int ledIdx = 0; ledIdx < 8; ledIdx++) {
    unoBuffer |= ledStatus[ledIdx] << bitNo;
    bitNo++;
  }
  Serial.println(unoBuffer, HEX);
  Wire.write(unoBuffer);
}
void setup() {
  Serial.begin(115200);
  Serial.println("UNO Started");
  for (int ledPin = 2; ledPin <= 9; ledPin++) {
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, ledStatus[ledPin - 2]);
  }
  Wire.begin(unoAddr);
  Wire.onReceive(i2cReceive);
  Wire.onRequest(i2cRequest);
}
void loop() {
}
