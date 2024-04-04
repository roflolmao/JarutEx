bool bFull = true;

void setup() {
  Serial.begin(115200);
  if (bFull) 
    Serial.println("ฉันจะโวยวาย");
  else
    Serial.println("ฉันกินต่อก่อนนะ");
}

void loop() {
}
