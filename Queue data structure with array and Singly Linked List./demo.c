const uint8_t queMaxElm = 5;
uint8_t queData[5];
uint8_t queElmCounter = 0;

bool queInit() {
  queElmCounter = 0;
  return true;
}

bool quePush( uint8_t x ) {
  if (queElmCounter == queMaxElm) {
    return false;
  }
  queData[queElmCounter] = x;
  queElmCounter += 1;
  return true;
}

bool quePop( uint8_t& x ) {
  if (queElmCounter == 0) {
    return false;
  }
  x = queData[0];
  queElmCounter -= 1;
  if (queElmCounter > 0) {
    for (int i = 0; i < queElmCounter; i++) {
      queData[i] = queData[i + 1];
    }
  }
  return true;
}

void queShow() {
  Serial.print("Queue data=[ ");
  for (int i = 0; i < queElmCounter; i++) {
    Serial.print(queData[i]);
    Serial.print(" ");
  }
  Serial.println("]");
}

void queDemo() {
  queInit();
  queShow();
  for (int i = 0; i < 6; i++) {
    Serial.print("push(");
    Serial.print(i);
    Serial.print(") ... ");
    if (quePush(i)) {
      Serial.println("done.");
      queShow();
    } else {
      Serial.println(" Queue overflow!");
    }
  }
  uint8_t data;
  for (int i = 0; i < 6; i++) {
    Serial.print("pop() ... ");
    if (quePop(data)) {
      Serial.println(data);
      queShow();
    } else {
      Serial.println(" Queue underflow!");
    }
  }
}

void setup() {
  Serial.begin( 9600 );

}

void loop() {
  queDemo();
  delay(30000);
}
