int score = 80;

void setup() {
  Serial.begin(115200);
  Serial.println("\n\n");
  if (score > 80)
    Serial.println("..ดีมากเลย..");
  else if (score > 60)
    Serial.println("..พอได้ ๆ..");
  else if (score > 30)
    Serial.println("...พอไหว...");
  else
    Serial.println("พอเถอะ");
}

void loop() {
}
