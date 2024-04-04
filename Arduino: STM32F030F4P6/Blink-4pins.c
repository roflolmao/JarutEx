// Blink-4pins
uint8_t pins[] = {PA0, PA1, PA2, PA3, PA4};

void setup() {
  for (int idx = 0; idx < 5; idx++) {
    pinMode( pins[idx], OUTPUT );
  }

}

void loop() {
  for (int idx = 0; idx < 5; idx++) {
    digitalWrite( pins[idx], !digitalRead( pins[idx] ));
  }
  delay(500);
}
