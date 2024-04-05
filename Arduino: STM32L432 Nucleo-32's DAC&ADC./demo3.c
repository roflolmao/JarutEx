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
  int degree = 0;
  float radian = 0.0;
  float sineValue = 0.0;
  int dValue = 0;
  for (degree = 0; degree < 360; degree++) {
    radian = (float)degree * (2.0 * 3.1415926) / 360.0;
    sineValue = sin(radian);
    dValue = (int)((1.0 + sineValue) * ((MAX_VALUE/2)-1));
    analogWrite( pinSpk, dValue );
    adcValue = analogRead(pinMic);
    Serial.println(adcValue);
  } 
}
