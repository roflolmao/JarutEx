#include <SPI.h>
#include <TFT_eSPI.h>
#include "SD.h"

TFT_eSPI tft = TFT_eSPI();

uint16_t colorsBg[] = {
  TFT_BLACK, TFT_NAVY, TFT_DARKGREEN, TFT_DARKCYAN,    
  TFT_MAROON, TFT_PURPLE,TFT_OLIVE,  TFT_LIGHTGREY,  
  TFT_DARKGREY,TFT_BLUE,TFT_GREEN, TFT_CYAN,TFT_RED,
  TFT_MAGENTA,TFT_YELLOW,TFT_WHITE,TFT_ORANGE,
  TFT_GREENYELLOW,TFT_PINK, TFT_BROWN, TFT_GOLD,
  TFT_SILVER,TFT_SKYBLUE, TFT_VIOLET  
};
uint16_t colorsFg[] = {
  TFT_WHITE - TFT_BLACK,
  TFT_WHITE - TFT_NAVY, 
  TFT_WHITE - TFT_DARKGREEN, 
  TFT_WHITE - TFT_DARKCYAN, 
  TFT_WHITE - TFT_MAROON, 
  TFT_WHITE - TFT_PURPLE,  
  TFT_WHITE - TFT_OLIVE, 
  TFT_WHITE - TFT_LIGHTGREY, 
  TFT_BLACK,
  TFT_WHITE - TFT_BLUE,  
  TFT_WHITE - TFT_GREEN,
  TFT_WHITE - TFT_CYAN, 
  TFT_WHITE - TFT_RED,
  TFT_WHITE - TFT_MAGENTA,
  TFT_WHITE - TFT_YELLOW,
  TFT_WHITE - TFT_WHITE , 
  TFT_WHITE - TFT_ORANGE, 
  TFT_WHITE - TFT_GREENYELLOW, 
  TFT_WHITE - TFT_PINK,
  TFT_WHITE - TFT_BROWN, 
  TFT_WHITE - TFT_GOLD, 
  TFT_WHITE - TFT_SILVER, 
  TFT_WHITE - TFT_SKYBLUE,
  TFT_WHITE - TFT_VIOLET
};

char colorsName[][16] = {
  {"TFT_BLACK"} ,{"TFT_NAVY"}, {"TFT_DARKGREEN"}, {"TFT_DARKCYAN"}, {"TFT_MAROON"},
  {"TFT_PURPLE"}, {"TFT_OLIVE"}, {"TFT_LIGHTGREY"}, {"TFT_DARKGREY"}, {"TFT_BLUE"},
  {"TFT_GREEN"}, {"TFT_CYAN"}, {"TFT_RED"}, {"TFT_MAGENTA"}, {"TFT_YELLOW"},
  {"TFT_WHITE"}, {"TFT_ORANGE"}, {"TFT_GREENYELLOW"}, {"TFT_PINK"}, {"TFT_BROWN"},
  {"TFT_GOLD"}, {"TFT_SILVER"}, {"TFT_SKYBLUE"}, {"TFT_VIOLET"}
};

int colorIdx = 0;
char msg[32];
uint8_t cardType;
uint64_t cardSize = 0;
bool sdCardStatus = true;

void setup() {

  pinMode( SW1, INPUT );
  pinMode( SW2, INPUT);

  if (!SD.begin()) {
    sdCardStatus = false;
  }

  tft.init();
  tft.setRotation(1);
  tft.writecommand(ST7735_MADCTL);
  tft.writedata(TFT_MAD_MV | TFT_MAD_COLOR_ORDER );

  if (sdCardStatus) {
    cardType = SD.cardType();

    if (cardType == CARD_NONE) {
      tft.fillScreen( TFT_RED );
      tft.setTextColor( TFT_YELLOW );
      tft.drawString( "ERROR", 40, 8, 4);
      tft.setTextColor( TFT_WHITE );
      tft.drawString("No SD card attached!", 30, 44, 2);
    } else {
      tft.fillScreen( TFT_BLACK );
      tft.setTextColor( TFT_YELLOW );
      tft.drawString("SD Card", 40, 8, 4);
      tft.setTextColor(TFT_WHITE);
      tft.drawString("Type", 30, 40, 2);
      tft.setTextColor(TFT_CYAN);
      if (cardType == CARD_MMC) {
        tft.drawString("MMC", 80, 40, 2);
      } else if (cardType == CARD_SD) {
        tft.drawString("SDSC", 80, 40, 2);
      } else if (cardType == CARD_SDHC) {
        tft.drawString("SDHC", 80, 40, 2);
      } else {
        tft.drawString("UNKNOWN", 80, 40, 2);
      }
      cardSize = SD.cardSize();
      tft.setTextColor(TFT_WHITE);
      tft.drawString("Size", 30, 60, 2);
      tft.setTextColor(TFT_CYAN);
      tft.drawNumber( cardSize / (1024 * 1024), 80, 60, 2);
      tft.setTextColor(TFT_WHITE);
      tft.drawString("MB", 120, 60, 2);
    }
  } else {
    tft.fillScreen( TFT_RED );
    tft.setTextColor( TFT_YELLOW );
    tft.drawString( "ERROR", 40, 8, 4);
    tft.setTextColor( TFT_WHITE );
    tft.drawString(" SD Card Mount failed!", 10, 44, 2);
  }
  delay(10000);
}

void loop() {

  tft.fillScreen( colorsBg[colorIdx] );
  tft.setTextColor( colorsFg[colorIdx] );
  tft.drawString( colorsName[colorIdx], 10 , 16,  2  ); // Font No.2
  tft.drawString( colorsName[colorIdx], 11 , 16,  2  ); // Font No.2
  delay(3000);
  colorIdx++;
  if (colorIdx == 24) {
    colorIdx = 0;
  }
}
