#include <Arduino.h>
uint8_t leds[] = {2, 3, 4, 5, 6, 7, 8, 9};
void setup() {
  Serial.begin( 115200 );
  for (int i = 0; i < 8; i++) {
    pinMode( leds[i], OUTPUT );
    digitalWrite( leds[i], LOW );
  }
}

void loop() {
  if (Serial.available()) {
    // มีข้อมูล
    String s = Serial.readString();
    // Serial.print(s);
    uint8_t x = s.toInt();
    if (x & 0b00000001) {
      digitalWrite( leds[0], HIGH );
    } else {
      digitalWrite( leds[0], LOW );
    }
    if (x & 0b00000010) {
      digitalWrite( leds[1], HIGH );
    } else {
      digitalWrite( leds[1], LOW );
    }
    if (x & 0b00000100) {
      digitalWrite( leds[2], HIGH );
    } else {
      digitalWrite( leds[2], LOW );
    }
    if (x & 0b00001000) {
      digitalWrite( leds[3], HIGH );
    } else {
      digitalWrite( leds[3], LOW );
    }
    if (x & 0b00010000) {
      digitalWrite( leds[4], HIGH );
    } else {
      digitalWrite( leds[4], LOW );
    }
    if (x & 0b00100000) {
      digitalWrite( leds[5], HIGH );
    } else {
      digitalWrite( leds[5], LOW );
    }
    if (x & 0b01000000) {
      digitalWrite( leds[6], HIGH );
    } else {
      digitalWrite( leds[6], LOW );
    }
    if (x & 0b10000000) {
      digitalWrite( leds[7], HIGH );
    } else {
      digitalWrite( leds[7], LOW );
    }
  }
}
