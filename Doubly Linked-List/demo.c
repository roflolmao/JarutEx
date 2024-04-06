#include <Arduino.h>
#include <DHT.h>
DHT dht = DHT(2, DHT11);

struct dNode {
  float t;
  float h;
  dNode * next;
  dNode * prev;
};

dNode *rootNode = NULL;
dNode *lastNode = NULL;
dNode *newNode = NULL;
int countNode = 0;

void printNode( dNode *n ) {
  Serial.print("[");
  Serial.print(n->t);
  Serial.print(",");
  Serial.print(n->h);
  Serial.print("][");
  Serial.print((int)(n->next));
  Serial.println("]");
}

void printList( dNode *r) {
  int counter = 0;
  dNode * currentNode = r;
  while (currentNode) {
    counter++;
    Serial.print("Node No.");
    Serial.print(counter);
    Serial.print(" address = ");
    Serial.print((int)currentNode);
    Serial.print(" T = ");
    Serial.print(currentNode->t);
    Serial.print("C H = ");
    Serial.print(currentNode->h);
    Serial.print("% prev = ");
    Serial.print((int)currentNode->prev);
    Serial.print(", next = ");
    Serial.println((int)currentNode->next);
    currentNode = currentNode->next;
  }
}

void addNode() {
  if (countNode == 10) {
    delete1stNode();
    countNode--;
  }
  newNode = (dNode*)malloc(sizeof(dNode));
  if (newNode) {
    newNode->t = dht.readTemperature();
    newNode->h = dht.readHumidity();
    newNode->next = NULL;
    newNode->prev = NULL;

    if (rootNode == NULL) {
      rootNode = newNode;
      lastNode = newNode;
    } else {
      newNode->prev = lastNode;
      lastNode->next = newNode;
      lastNode = newNode;
    }
    countNode++;
  } else {
    Serial.print("Not enough memory!");
    while (1) {
    }
  }
}

void delete1stNode() {
  newNode = rootNode;
  rootNode = newNode->next;
  rootNode->prev = NULL;
  free(newNode);
}

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  addNode();
  Serial.println("------------------------------");
  printList(rootNode);  
  delay(2000);
}
