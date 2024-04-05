#include <SPI.h>
#include <TFT_eSPI.h>
#include "SD_MMC.h"
#include "soc/soc.h"           // Disable brownour problems
#include "soc/rtc_cntl_reg.h"  // Disable brownour problems
#include "driver/rtc_io.h"
#include <EEPROM.h>            // read and write from flash memory

// Use hardware SPI
TFT_eSPI tft = TFT_eSPI();

#define SW1 0
#define SW2 16

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

inline bool sw(int swX) {
  return (1 - digitalRead(swX));
}

void waitKey() {
  while (true) {
    if (sw(SW1) || sw(SW2)) {
      break;
    }
  }
}

void errorMsg(char title[32], char detail[64]) {
  while (true) {
    tft.fillScreen( TFT_RED  );
    tft.setTextColor( TFT_YELLOW );
    tft.drawString( title, 20 , 10, 4 );
    tft.drawString( title , 21 , 10, 4 );
    tft.setTextColor( TFT_WHITE );
    tft.drawString( detail, 20 , 40, 2 );
    waitKey();
    delay(500);
    tft.fillScreen( TFT_BLACK  );
    tft.setTextColor( TFT_YELLOW );
    tft.drawString( title, 20 , 10, 4 );
    tft.drawString( title , 21 , 10, 4 );
    tft.setTextColor( TFT_WHITE );
    tft.drawString( detail, 20 , 40, 2 );
    waitKey();
    delay(250);
  }
}

void setup() {
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0); //disable brownout detector
  pinMode( SW1, INPUT );
  pinMode( SW2, INPUT);

  if (!SD_MMC.begin()) {
    sdCardStatus = false;
  }
  
  tft.init();
  tft.setRotation(3);


  if (sdCardStatus) {
    cardType = SD_MMC.cardType();

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
      cardSize = SD_MMC.cardSize();
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
  waitKey();
}

void loop() {
  tft.fillScreen( colorsBg[colorIdx] );
  tft.setTextColor( colorsFg[colorIdx] );
  tft.drawString( colorsName[colorIdx], 10 , 16,  2  ); // Font No.2
  tft.drawString( colorsName[colorIdx], 11 , 16,  2  ); // Font No.2
  sprintf(msg, "Sw2 = %d, Sw3 = %d\n", digitalRead( 0 ), digitalRead( 16 ));
  tft.drawString( msg, 10, 48 );
  delay(3000);
  colorIdx++;
  if (colorIdx == 24) {
    colorIdx = 0;
  }
}
