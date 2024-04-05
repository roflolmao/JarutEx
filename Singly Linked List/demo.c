struct sNode {
  float t;
  float h;
  sNode * next;
};

sNode *rootNode;
sNode *currentNode;
sNode *newNode;

void printNode( sNode *n ) {
  Serial.print("[");
  Serial.print(n->t);
  Serial.print(",");
  Serial.print(n->h);
  Serial.print("][");
  Serial.print((int)(n->next));
  Serial.println("]");
}

void setup() {
  rootNode = NULL;
  Serial.begin(9600);
  long count = 0;
  do {
    newNode = (sNode*)malloc(sizeof(sNode));
    if (newNode) {
      newNode->t = 0.0;
      newNode->h = 0.0;
      newNode->next = NULL;
      if (rootNode == NULL) {
        rootNode = newNode;
        currentNode = newNode;
      } else {
        currentNode->next = newNode;
        currentNode = newNode;
      }
      count++;
      Serial.print(".");
    }
  } while (newNode != NULL);

  Serial.println();
  Serial.print("Number of node(s) = ");
  Serial.println(count);

  currentNode = rootNode;
  while (currentNode) {
    Serial.print("This = ");
    Serial.print((int)currentNode);
    Serial.print("Next = ");
    Serial.println((int)currentNode->next);
    currentNode = currentNode->next;
  }
}

void loop() {

}
