void setup() {
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop() {
  for (int i = 3; i < 6; i++) {
    digitalWrite(i, LOW);
    delay(250);
    digitalWrite(i, HIGH);
    delay(250);
  }
}
