#include <Arduino.h>
#include <SPI.h>
#include <TFT_eSPI.h>

TFT_eSPI tft = TFT_eSPI();


uint16_t colorsBg[] = {
  TFT_BLACK,     /*   0,   0,   0 */
  TFT_NAVY,      /*   0,   0, 128 */
  TFT_DARKGREEN,    /*   0, 128,   0 */
  TFT_DARKCYAN,      /*   0, 128, 128 */
  TFT_MAROON,      /* 128,   0,   0 */
  TFT_PURPLE,      /* 128,   0, 128 */
  TFT_OLIVE,      /* 128, 128,   0 */
  TFT_LIGHTGREY,      /* 211, 211, 211 */
  TFT_DARKGREY,      /* 128, 128, 128 */
  TFT_BLUE,      /*   0,   0, 255 */
  TFT_GREEN, /*   0, 255,   0 */
  TFT_CYAN,/*   0, 255, 255 */
  TFT_RED,/* 255,   0,   0 */
  TFT_MAGENTA,/* 255,   0, 255 */
  TFT_YELLOW,/* 255, 255,   0 */
  TFT_WHITE ,/* 255, 255, 255 */
  TFT_ORANGE,/* 255, 180,   0 */
  TFT_GREENYELLOW, /* 180, 255,   0 */
  TFT_PINK, /* 255, 192, 203 */ //Lighter pink, was 0xFC9F
  TFT_BROWN, /* 150,  75,   0 */
  TFT_GOLD, /* 255, 215,   0 */
  TFT_SILVER, /* 192, 192, 192 */
  TFT_SKYBLUE, /* 135, 206, 235 */
  TFT_VIOLET  /* 180,  46, 226 */
};
uint16_t colorsFg[] = {
  TFT_WHITE - TFT_BLACK,   /*   0,   0,   0 */
  TFT_WHITE - TFT_NAVY,    /*   0,   0, 128 */
  TFT_WHITE - TFT_DARKGREEN,  /*   0, 128,   0 */
  TFT_WHITE - TFT_DARKCYAN,    /*   0, 128, 128 */
  TFT_WHITE - TFT_MAROON,    /* 128,   0,   0 */
  TFT_WHITE - TFT_PURPLE,    /* 128,   0, 128 */
  TFT_WHITE - TFT_OLIVE,    /* 128, 128,   0 */
  TFT_WHITE - TFT_LIGHTGREY,    /* 211, 211, 211 */
  // TFT_WHITE - TFT_DARKGREY,    /* 128, 128, 128 */
  TFT_BLACK,
  TFT_WHITE - TFT_BLUE,    /*   0,   0, 255 */
  TFT_WHITE - TFT_GREEN, /*   0, 255,   0 */
  TFT_WHITE - TFT_CYAN, /*   0, 255, 255 */
  TFT_WHITE - TFT_RED, /* 255,   0,   0 */
  TFT_WHITE - TFT_MAGENTA, /* 255,   0, 255 */
  TFT_WHITE - TFT_YELLOW, /* 255, 255,   0 */
  TFT_WHITE - TFT_WHITE , /* 255, 255, 255 */
  TFT_WHITE - TFT_ORANGE, /* 255, 180,   0 */
  TFT_WHITE - TFT_GREENYELLOW, /* 180, 255,   0 */
  TFT_WHITE - TFT_PINK, /* 255, 192, 203 */ //Lighter pink, was 0xFC9F
  TFT_WHITE - TFT_BROWN, /* 150,  75,   0 */
  TFT_WHITE - TFT_GOLD, /* 255, 215,   0 */
  TFT_WHITE - TFT_SILVER, /* 192, 192, 192 */
  TFT_WHITE - TFT_SKYBLUE, /* 135, 206, 235 */
  TFT_WHITE - TFT_VIOLET /* 180,  46, 226 */
};

char colorsName[][16] = {
  {"TFT_BLACK"} ,
  {"TFT_NAVY"},
  {"TFT_DARKGREEN"},
  {"TFT_DARKCYAN"},
  {"TFT_MAROON"},
  {"TFT_PURPLE"},
  {"TFT_OLIVE"},
  {"TFT_LIGHTGREY"},
  {"TFT_DARKGREY"},
  {"TFT_BLUE"},
  {"TFT_GREEN"},
  {"TFT_CYAN"},
  {"TFT_RED"},
  {"TFT_MAGENTA"},
  {"TFT_YELLOW"},
  {"TFT_WHITE"},
  {"TFT_ORANGE"},
  {"TFT_GREENYELLOW"},
  {"TFT_PINK"},
  {"TFT_BROWN"},
  {"TFT_GOLD"},
  {"TFT_SILVER"},
  {"TFT_SKYBLUE"},
  {"TFT_VIOLET"}
};

int colorIdx = 0;
char msg[32];

void setup() {
  tft.init();
  tft.setRotation(1);
  tft.writecommand(TFT_MADCTL);
  tft.writedata(TFT_MAD_MV | TFT_MAD_COLOR_ORDER );
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
