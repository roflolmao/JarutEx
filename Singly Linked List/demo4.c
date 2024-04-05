#include <Arduino.h>
#include <DHT.h>
DHT dht = DHT(13, DHT11); // D13

struct sNode {
  float t;
  float h;
  sNode * next;
};

sNode *rootNode;
sNode *currentNode;
sNode *newNode;
int countNode;

void printNode( sNode *n ) {
  SerialUSB.print("[");
  SerialUSB.print(n->t);
  SerialUSB.print(",");
  SerialUSB.print(n->h);
  SerialUSB.print("][");
  SerialUSB.print((int)(n->next));
  SerialUSB.println("]");
}

void printList( sNode *r) {
  int counter = 0;
  sNode * currentNode = r;
  while (currentNode) {
    counter++;
    SerialUSB.print("Node No.");
    SerialUSB.print(counter);
    SerialUSB.print(" address = ");
    SerialUSB.print((int)currentNode);
    SerialUSB.print(" T = ");
    SerialUSB.print(currentNode->t);
    SerialUSB.print("C H = ");
    SerialUSB.print(currentNode->h);
    SerialUSB.print("% next = ");
    SerialUSB.println((int)currentNode->next);
    currentNode = currentNode->next;
  }
}

void addNode() {
  if (countNode == 10) {
    delete1stNode();
    countNode--;
  }
  newNode = (sNode*)malloc(sizeof(sNode));
  if (newNode) {
    newNode->t = dht.readTemperature();
    newNode->h = dht.readHumidity();
    newNode->next = NULL;
    if (rootNode == NULL) {
      rootNode = newNode;
      currentNode = newNode;
    } else {
      currentNode->next = newNode;
      currentNode = newNode;
    }
    countNode++;
  } else {
    SerialUSB.print("Not enough memory!");
    while (1) {
    }
  }
}

void delete1stNode() {
  newNode = rootNode;
  rootNode = newNode->next;
  free(newNode);
}

void setup() {
  countNode = 0;
  rootNode = NULL;
  SerialUSB.begin(9600);
  dht.begin();
}

void loop() {
  addNode();
  SerialUSB.println("------------------------------");
  printList(rootNode);  
  delay(2000);
}
