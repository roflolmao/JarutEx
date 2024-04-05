#include <Arduino.h>

#define pinSpk DAC1
#define pinMic 1
#define MAX_DAC_VALUES 200 // 256
#define MAX_ADC_VALUES 4096

int adcValue;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
}

void loop() {
for (int i = 0; i < MAX_DAC_VALUES; i++) {
    dacWrite( pinSpk, i );
    adcValue = analogRead(pinMic);
    Serial.println(adcValue);
  }
  for (int i = MAX_DAC_VALUES-1; i >= 0; i--) {
    dacWrite( pinSpk, i );
    adcValue = analogRead(pinMic);
    Serial.println(adcValue);
  }
}
