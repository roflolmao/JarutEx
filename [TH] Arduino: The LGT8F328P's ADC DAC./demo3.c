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
  int degree = 0;
  float radian = 0.0;
  float sineValue = 0.0;
  int dValue = 0;

  for (degree = 0; degree < 360; degree++) {
    radian = (float)degree * (2.0 * 3.1415926) / 360.0;
    sineValue = sin(radian);
    dValue = (int)((1.0 + sineValue) * 125.0);
    analogWrite( pinSpk, dValue );
    adcValue = analogRead(pinMic);
    Serial.println(adcValue);
  }  
}
