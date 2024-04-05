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

void printList( sNode *r) {
  sNode * currentNode = r;
  while (currentNode) {
    Serial.print("This = ");
    Serial.print((int)currentNode);
    Serial.print(" next = ");
    Serial.println((int)currentNode->next);
    currentNode = currentNode->next;
  }
}

void setup() {
  rootNode = NULL;
  Serial.begin(9600);
  int count = 0;

  // Add 5 nodes
  for (count = 0; count < 5; count++) {
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
      Serial.print(".");
    } else {
      Serial.print("Not enough memory!");
      while (1) {

      }
    }
  }
  // show all nodes
  Serial.println();
  Serial.println("The 5 nodes:");
  printList( rootNode );

  // Delete the 1st node
  newNode = rootNode;
  rootNode = newNode->next;
  free(newNode);
  Serial.println("After deleted the 1st node.");
  printList( rootNode );

  // Delete the 2nd node
  newNode = rootNode->next;
  rootNode->next = newNode->next;
  free(newNode);
  Serial.println("After deleted the 2st node.");
  printList( rootNode );

  // Delete the last node
  newNode = rootNode;
  while (newNode->next != currentNode) {
    newNode = newNode->next;
  }
  newNode->next = NULL;
  free(currentNode);
  Serial.println("After deleted the last node.");
  currentNode = newNode;
  printList( rootNode );
}

void loop() {

}
