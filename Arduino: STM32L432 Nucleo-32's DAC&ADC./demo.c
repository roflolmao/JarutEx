#include <Arduino.h>
#include <math.h>

#define pinSpk A3 // PA4
#define pinMic D3 // PB0

#define ADC_BITS 12
#define DAC_BITS 12
#define MAX_VALUE pow(2,DAC_BITS)

int adcValue;

void setup() {
  Serial.begin(115200);
  analogReadResolution(ADC_BITS);
  analogWriteResolution(DAC_BITS);
}

void loop() {
  for (int i = 0; i < MAX_VALUE; i += 16) {
    analogWrite( pinSpk, i);
    adcValue = analogRead(pinMic);
    Serial.println(adcValue);
  }
}
