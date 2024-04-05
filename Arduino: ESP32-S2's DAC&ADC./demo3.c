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
  int degree = 0;
  float radian = 0.0;
  float sineValue = 0.0;
  int dValue = 0;

  for (degree = 0; degree < 360; degree++) {
    radian = (float)degree * (2.0 * 3.1415926) / 360.0;
    sineValue = sin(radian);
    dValue = (int)((1.0 + sineValue) * (MAX_DAC_VALUES/2));
    dacWrite( pinSpk, dValue );
    adcValue = analogRead(pinMic);
    Serial.println(adcValue);
  }
}
