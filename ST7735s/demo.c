#include <TFT_eSPI.h> // Graphics and font library for ST7735 driver chip
#include <SPI.h>
TFT_eSPI tft = TFT_eSPI();  // Invoke library, pins defined in User_Setup.h

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

void setup() {
  tft.init();
  tft.setRotation(1);
  tft.writecommand(ST7735_MADCTL);
  tft.writedata(TFT_MAD_MV | TFT_MAD_COLOR_ORDER );
  tft.fillScreen(0x3861);
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
