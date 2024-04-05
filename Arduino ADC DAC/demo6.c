#include <Arduino.h>

#define pinSpk 26
#define pinMic 36
int adcValue;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
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
    dacWrite( pinSpk, dValue );
    adcValue = analogRead(pinMic);
    Serial.println(adcValue);
  }
}
