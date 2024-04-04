#include <Arduino.h>
#include <math.h>

#define pi 3.141592654

void setup() {
  pinMode(4, ANALOG);     // D4 
  analogReference(INTERNAL4V096);   //Internal reference source 4.096V 
}

void loop() {
 for(float i=0;i<(2*pi); i+=0.01) {
  float rad=pi*i;    
  float cosValue = cos(rad);
  long intCosValue = cosValue*300;
  byte dacValue = map(intCosValue,-300,300,0,255);
  analogWrite(4, dacValue);
  }
}
