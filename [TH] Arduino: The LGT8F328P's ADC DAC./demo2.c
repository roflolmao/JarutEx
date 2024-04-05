#include <Arduino.h>

#define pinSpk DAC0 // D4
#define pinMic A0
#define MAX_VALUE 255
#define ADC_BITS 12

int adcValue;

void setup() {
  Serial.begin(9600);
  analogReadResolution(ADC_BITS);
  analogReference(DEFAULT);  // 5v
  pinMode(DAC0, ANALOG);
}

void loop() {
  int i;
  for (i = 0; i < MAX_VALUE+1; i ++) {
    analogWrite( pinSpk, i);
    adcValue = analogRead(pinMic);
    Serial.println(adcValue);
  }
  for (i = MAX_VALUE-1; i >= 0; i--) {
    analogWrite( pinSpk, i);
    adcValue = analogRead(pinMic);
    Serial.println(adcValue);
  }
}
