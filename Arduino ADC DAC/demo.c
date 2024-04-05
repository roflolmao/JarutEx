#include <Arduino.h>

#define pinSpk A0
#define pinMic A1
int adcValue;

void setup() {
  SerialUSB.begin(115200);
  analogReadResolution(12);
  analogWriteResolution(10);

}

void loop() {
  for (int i = 0; i < 1024; i += 4) {
    analogWrite( pinSpk, i);
    adcValue = analogRead(pinMic);
    SerialUSB.println(adcValue);
  }
}
