#include <SPI.h>
#include <TFT_eSPI.h>
#include <DHT.h>

TFT_eSPI tft = TFT_eSPI();
DHT dht = DHT(PB13, DHT11);

struct sNode {
  float t;
  float h;
  sNode * next;
};

sNode *rootNode = NULL;
sNode *currentNode = NULL;
sNode *newNode = NULL;
int countNode = 0;
float tAvg = 0.0;
float hAvg = 0.0;
float tMax = 0.0;
float tMin = 101.0;
float hMax = 0.0;
float hMin = 101.0;

void addNode() {
  if (countNode == 10) {
    delete1stNode();
    countNode--;
  }
  newNode = (sNode*)malloc(sizeof(sNode));
  if (newNode) {
    newNode->t = dht.readTemperature();
    newNode->h = dht.readHumidity();
    if (tMin > newNode->t) {
      tMin = newNode->t;
    }
    if (tMax < newNode->t) {
      tMax = newNode->t;
    }
    if (hMin > newNode->h) {
      hMin = newNode->h;
    }
    if (hMax < newNode->h) {
      hMax = newNode->h;
    }
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
    tft.fillScreen( TFT_RED );
    tft.setTextColor( TFT_YELLOW );
    tft.drawString( "ERROR", 40, 8, 4);
    tft.setTextColor( TFT_WHITE );
    tft.drawString("Not enough memory!", 4, 44, 2);
    while (1) {
    }
  }
}

void delete1stNode() {
  newNode = rootNode;
  rootNode = newNode->next;
  free(newNode);
}

void findAverage() {
  float tSum = 0.0;
  float hSum = 0.0;
  sNode * p;
  p = rootNode;
  for (int idx = 0; idx < countNode; idx++) {
    tSum += p->t;
    hSum += p->h;
    p = p->next;
  }
  tAvg = tSum / (float)countNode;
  hAvg = hSum / (float)countNode;
}

void drawScreen() {
  int newTemMin, newTemMax;
  int newHumMin, newHumMax;
  int newTem;
  int newHum;
  int newTemAvg, newHumAvg;
  sNode * p;
  p = rootNode;

  tft.fillRect(4, 25, 152, 51, TFT_NAVY);
  // scale
  newTemMin = map((int)tMin, 0, 100, 75, 25);
  newTemMax = map((int)tMax, 0, 100, 75, 25);
  newHumMin = map((int)hMin, 0, 100, 75, 25);
  newHumMax = map((int)hMax, 0, 100, 75, 25);
  newTemAvg = map((int)tAvg, 0, 100, 75, 25);
  newHumAvg = map((int)hAvg, 0, 100, 75, 25);
  // draw
  tft.drawLine(5, newTemMin, 155, newTemMin, TFT_LIGHTGREY);
  tft.drawLine(5, newTemMax, 155, newTemMax, TFT_BROWN);
  tft.drawLine(5, newHumMin, 155, newHumMin, TFT_SILVER);
  tft.drawLine(5, newHumMax, 155, newHumMax, TFT_SKYBLUE);
  tft.drawLine(5, newTemAvg, 155, newTemAvg, TFT_GOLD);
  tft.drawLine(5, newHumAvg, 155, newHumAvg, TFT_ORANGE);
  //
  int oldTem, oldHum;
  int xStep = 15;
  int xStart = 5;
  for (int idx = 0; idx < countNode; idx++) {
    newTem = map((int)p->t, 0, 100, 75, 25);
    newHum = map((int)p->h, 0, 100, 75, 25);
    if (idx == 0) {
      tft.drawLine(xStart + idx * xStep, newTem, xStart + (idx + 1)*xStep, newTem, TFT_CYAN);
      tft.drawLine(xStart + idx * xStep, newHum, xStart + (idx + 1)*xStep, newHum, TFT_YELLOW);
    } else {
      tft.drawLine(xStart + idx * xStep, oldTem, xStart + (idx + 1)*xStep, newTem, TFT_CYAN);
      tft.drawLine(xStart + idx * xStep, oldHum, xStart + (idx + 1)*xStep, newHum, TFT_YELLOW);
    }
    oldTem = newTem;
    oldHum = newHum;
    p = p->next;
  }
}

void setup() {
  tft.init();
  dht.begin();

  tft.setRotation(1);
  tft.writecommand(ST7735_MADCTL);
  tft.writedata(TFT_MAD_MV | TFT_MAD_COLOR_ORDER );

  tft.fillScreen( TFT_BLACK );
  tft.setTextColor( TFT_GREEN );
  tft.fillRect(0, 0, 160, 20, TFT_MAROON);
  tft.drawString( "temperature/humidity", 14, 1, 2);
  tft.fillRect(0, 21, 160, 60, TFT_DARKGREY);
}

void loop() {
  addNode();
  findAverage();
  drawScreen();
  for (int i=0; i<15; i++) {
    delay(60000); // 1-minute
  }
}
