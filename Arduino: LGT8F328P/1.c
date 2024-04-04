#include <Arduino.h>
#define pinADC A0
void setup() {
  Serial.begin(115200);
  pinMode( pinADC, INPUT );
}

void loop() {
  int aValue = analogRead( pinADC );
  float approxVDC = 3.3*(aValue/1024.0);
  Serial.print("ADC value = ");
  Serial.print(aValue);
  Serial.print(" approximate V = ");
  Serial.println(approxVDC);
  delay(1000);
}
