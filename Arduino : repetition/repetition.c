// repetition: demo while
void setup() {
  word sum=0;
  word counter=0;
  word endNumber = 100;
  Serial.begin(115200);
  Serial.println("---------- Begin of program ------------");
  Serial.print("Before: sum = ");
  Serial.println(sum);
  while (counter <= endNumber) {
    sum += counter;
    counter += 1;
  }
  Serial.print("After: sum = ");
  Serial.println(sum);
  Serial.println("----------  End of Program  ------------");
}

void loop() {
}
