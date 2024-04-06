const uint8_t queMaxElm = 5;
struct queNode {
  uint8_t data;
  queNode * next;
};

queNode * queRoot;
queNode * queCurrentNode;
queNode * queNewNode;
uint8_t queElmCounter = 0;

bool queInit() {
  queElmCounter = 0;
  queRoot = NULL;
  queCurrentNode = NULL;
  queNewNode = NULL;
  return true;
}

bool quePush( uint8_t x ) {
  if (queElmCounter == queMaxElm) {
    return false;
  }
  queNewNode = (queNode*)malloc( sizeof( queNode ) );
  if (queNewNode == NULL) {
    return false;
  }
  queNewNode->next = NULL;
  queNewNode->data = x;
  if (queElmCounter == 0) {
    queRoot = queNewNode;
  } else {
    queCurrentNode->next = queNewNode;
  }
  queCurrentNode = queNewNode;
  queElmCounter += 1;
  return true;
}

bool quePop( uint8_t& x ) {
  if (queElmCounter == 0) {
    return false;
  }

  if (queRoot == queCurrentNode) {
    x = queRoot->data;
    free(queRoot);
    queRoot = NULL;
    queCurrentNode = NULL;
  } else {
    queNode * p = queRoot;
    x = p->data;
    queRoot = p->next;
    free(p);
  }
  queElmCounter -= 1;
  return true;
}

void queShow() {
  Serial.print("Queue data=[ ");
  queNode * currentNode = queRoot;
  while (currentNode) {
    Serial.print(currentNode->data);
    Serial.print(" ");
    currentNode = currentNode->next;
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
      Serial.println(" Queue overflow! or not enough memory!");
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
