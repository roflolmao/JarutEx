const uint8_t stkMaxElm = 5;
uint8_t stkData[5];
uint8_t stkElmCounter = 0;

bool stkInit() {
  stkElmCounter = 0;
  return true;
}

bool stkPush( uint8_t x ) {
  if (stkElmCounter == stkMaxElm) {
    return false;
  }
  stkData[stkElmCounter] = x;
  stkElmCounter += 1;
  return true;
}

bool stkPop( uint8_t& x ) {
  if (stkElmCounter == 0) {
    return false;
  }
  x = stkData[stkElmCounter - 1];
  stkElmCounter -= 1;
  return true;
}

void stkShow() {
  Serial.print("Stack data=[ ");
  for (int i = 0; i < stkElmCounter; i++) {
    Serial.print(stkData[i]);
    Serial.print(" ");
  }
  Serial.println("]");
}

void setup() {
  Serial.begin( 9600 );
  stkInit();
  stkShow();
  for (int i = 0; i < 6; i++) {
    Serial.print("push(");
    Serial.print(i);
    Serial.print(") ... ");
    if (stkPush(i)) {
      Serial.println("done.");
      stkShow();
    } else {
      Serial.println(" Stack overflow!");
    }
  }
  uint8_t data;
  for (int i = 0; i < 6; i++) {
    Serial.print("pop() ... ");
    if (stkPop(data)) {
      Serial.println(data);
      stkShow();
    } else {
      Serial.println(" Stack underflow!");
    }
  }
}

void loop() {
}
