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
  for (int i = 0; i < 1024; i += 8) {
    analogWrite( pinSpk, i);
    adcValue = analogRead(pinMic);
    SerialUSB.println(adcValue);
  }
  for (int i = 1023; i >= 0; i -= 8) {
    analogWrite( pinSpk, i);
    adcValue = analogRead(pinMic);
    SerialUSB.println(adcValue);
  }
}
