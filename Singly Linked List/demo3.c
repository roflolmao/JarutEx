#include <DHT.h>
DHT dht = DHT(D2, DHT11);

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
  Serial.print("[");
  Serial.print(n->t);
  Serial.print(",");
  Serial.print(n->h);
  Serial.print("][");
  Serial.print((int)(n->next));
  Serial.println("]");
}

void printList( sNode *r) {
  int counter = 0;
  sNode * currentNode = r;
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
    Serial.print("% next = ");
    Serial.println((int)currentNode->next);
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
    Serial.print("Not enough memory!");
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
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  addNode();
  Serial.println("------------------------------");
  printList(rootNode);  
  delay(2000);
}
