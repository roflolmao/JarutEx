/*
 * esp32oled + GamePad
 * (C) 2021, JarutEx (https://www.jarutex.com)
 * 2021-07-06
*/

#include <Arduino.h>

#define PIN_VR_X 36
#define PIN_VR_Y 39
#define PIN_SW_A 2
#define PIN_SW_B 14
#define PIN_SW_C 13
#define PIN_SW_D 15
#define PIN_SW_E 16
#define PIN_SW_F 26
#define MAX_SW 6

uint8_t swPins[MAX_SW] = {PIN_SW_A,PIN_SW_B,PIN_SW_C,PIN_SW_D,PIN_SW_E,PIN_SW_F};
uint8_t swValues[MAX_SW];
uint8_t vrPins[2] = {PIN_VR_X, PIN_VR_Y};
uint16_t vrValues[2];

void setup() {
  for (int i=0; i<MAX_SW; i++) {
    pinMode( swPins[i], INPUT_PULLUP );
    swValues[i] = 1;
  }
  Serial.begin(9600);
}

void doUpdate() {
  for (int i=0; i<MAX_SW; i++) {
    swValues[i] = digitalRead( swPins[i] );
  }
  vrValues[0] = analogRead( vrPins[0] );
  vrValues[1] = analogRead( vrPins[1] );  
}

void doShow() {
  Serial.print(vrValues[0]);
  Serial.print(",");
  Serial.print(vrValues[1]);
  Serial.print(":");
  for (int i=0; i<MAX_SW; i++) {
    Serial.print(swValues[i]);
    if (i<(MAX_SW-1)) {
      Serial.print("/");
    }
  }
  Serial.println();
}

void loop() {
  doUpdate();
  doShow();
  delay(250);
}
