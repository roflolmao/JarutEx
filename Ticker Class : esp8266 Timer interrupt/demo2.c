#include <Ticker.h>

Ticker tm500ms;

void  myToggle() {
  int state = digitalRead(LED_BUILTIN);  // get the current state of GPIO1 pin
  digitalWrite(LED_BUILTIN, !state);     // set pin to the opposite state
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  tm500ms.attach(0.5, myToggle);
}

void loop() {
}
