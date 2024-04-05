/*
  Hello.ino

  Demonstrates how to use U8g2_for_TFT_eSPI library.

  U8g2_for_TFT_eSPI:
    - Use U8g2 fonts with TFT_eSPI
    - Supports UTF-8 in print statement
    - 90, 180 and 270 degree text direction
  
  List of all U8g2 fonts:    https://github.com/olikraus/u8g2/wiki/fntlistall

  TFT_eSPI library:          https://github.com/Bodmer/TFT_eSPI
  U8g2_for_TFT_eSPI library: https://github.com/Bodmer/U8g2_for_TFT_eSPI

*/
#include "SPI.h"
#include "TFT_eSPI.h"
#include "U8g2_for_TFT_eSPI.h"

TFT_eSPI tft = TFT_eSPI();   // tft instance
U8g2_for_TFT_eSPI u8f;       // U8g2 font instance

void setup() {
  tft.begin();
  tft.setRotation(1);
  tft.fillScreen(0x3861);

  u8f.begin(tft);                    
}

unsigned long x = 0;

void loop() {
  u8f.setFontMode(0);                 
  u8f.setFontDirection(0);         
  u8f.setForegroundColor(TFT_WHITE);  

  u8f.setFont(u8g2_font_helvR14_tf);  
  u8f.setCursor(0,20);              
  u8f.print("Hello World");
  u8f.setCursor(0,40);               
  u8f.print("Umlaut ÄÖÜ");           

  u8f.setBackgroundColor(0x3861);
  u8f.setForegroundColor(0xe717);
  u8f.setFont(u8g2_font_osb21_tf);
  u8f.setCursor(40,100);
  u8f.print("www.JarutEx.com");
  u8f.setForegroundColor(TFT_YELLOW);
  u8f.setCursor(20,100);
  u8f.print("~");
  u8f.setCursor(280,100);
  u8f.print("~");

  u8f.setFont(u8g2_font_inb63_mn);    
  u8f.setFontMode(0);                 
  u8f.setForegroundColor(TFT_WHITE); 

  while (1) {
    u8f.setCursor(0,200);  
    u8f.print(x);        
    x++;
    if (x > 99999) {
      x = 0;
    }
    delay(1000);
  }
} 
