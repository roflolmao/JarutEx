const uint8_t stkMaxElm = 5;
struct stkNode {
  uint8_t data;
  stkNode * next;
};

stkNode * stkRoot;
stkNode * stkCurrentNode;
stkNode * stkNewNode;
uint8_t stkElmCounter = 0;

bool stkInit() {
  stkElmCounter = 0;
  stkRoot = NULL;
  stkCurrentNode = NULL;
  stkNewNode = NULL;
  return true;
}

bool stkPush( uint8_t x ) {
  if (stkElmCounter == stkMaxElm) {
    return false;
  }
  stkNewNode = (stkNode*)malloc( sizeof( stkNode ) );
  if (stkNewNode == NULL) {
    return false;
  }
  stkNewNode->next = NULL;
  stkNewNode->data = x;
  if (stkElmCounter == 0) {
    stkRoot = stkNewNode;
  } else {
    stkCurrentNode->next = stkNewNode;
  }
  stkCurrentNode = stkNewNode;
  stkElmCounter += 1;
  return true;
}

bool stkPop( uint8_t& x ) {
  if (stkElmCounter == 0) {
    return false;
  }

  if (stkRoot == stkCurrentNode) {
    x = stkCurrentNode->data;
    free(stkCurrentNode);
    stkRoot = NULL;
    stkCurrentNode = NULL;
  } else {
    x = stkCurrentNode->data;

    stkNode * currentNode = stkRoot;
    while (currentNode->next != stkCurrentNode) {
      currentNode = currentNode->next;
    }
    currentNode->next = NULL;
    free(stkCurrentNode);
    stkCurrentNode = currentNode;
  }
  stkElmCounter -= 1;
  return true;
}

void stkShow() {
  Serial.print("Stack data=[ ");
  stkNode * currentNode = stkRoot;
  while (currentNode) {
    Serial.print(currentNode->data);
    Serial.print(" ");
    currentNode = currentNode->next;
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
      Serial.println(" Stack overflow! or not enough memory!");
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
