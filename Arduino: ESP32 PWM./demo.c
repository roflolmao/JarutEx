#include <Arduino.h>

#define spk 19
#define spkCh 0
#define keL 39
#define keU 34
#define keD 35
#define keR 32
#define swM1 33
#define swM2 25
#define swA 26
#define swB 27

uint8_t input[] = {
  keL, keU,  keD, keR, swM1, swM2, swA, swB
};

uint16_t freq[] = {
  523, 587, 659, 698, 784, 880, 988, 1047
};

void setup() {
  Serial.begin(115200);
  int i;
  for (i = 0; i < 8; i++) {
    pinMode(input[i], INPUT_PULLUP);
  }
  pinMode( spk, OUTPUT );
  ledcSetup( spkCh, 0, 8 );
  ledcAttachPin( spk, spkCh );
}

int8_t pressed = 0;
void loop() {
  for (int idx = 0; idx < 8; idx++) {
    if (digitalRead( input[idx] ) == 0) {
      if (pressed == idx + 1) {
        ledcWrite( spkCh, 100 );
        break;
      }
      ledcSetup( spkCh, freq[idx], 8 );
      ledcAttachPin( spk, spkCh );
      ledcWrite( spkCh, 100 );
      pressed = idx + 1;
      Serial.printf("%d [%d] pressed\n", input[idx], freq[idx]);
      break;
    }
  }
  delay(200);
  ledcWrite( spkCh, 0 );
}
