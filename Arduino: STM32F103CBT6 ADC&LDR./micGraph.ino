// micGraph.ino
// JarutEx
#include <TFT_eSPI.h> // Graphics and font library for ST7735 driver chip
#include <SPI.h>
TFT_eSPI tft = TFT_eSPI();  // Invoke library, pins defined in User_Setup.h

#define textColor TFT_WHITE
#define textBgColor 0x3861
#define pinMic PA0
#define ADC_BITS 12

String msg;
uint16_t dValue;

void setup() {
  analogReadResolution(ADC_BITS);
  tft.init();
  tft.setRotation(1);
  tft.writecommand(ST7735_MADCTL);
  tft.writedata(TFT_MAD_MV | TFT_MAD_COLOR_ORDER );
  tft.fillScreen(textBgColor);
}

void loop() {
  dValue = analogRead( pinMic );
  msg = "ADC value=";
  msg += dValue;
  
  tft.fillScreen( textBgColor );
  tft.setTextColor( textColor );
  tft.drawString( msg, 8 , 40,  1  ); // Font No.1
  delay(3000);
  tft.fillScreen( textBgColor );
  tft.setTextColor( textColor );
  tft.drawString( msg, 8 , 40,  2  ); // Font No.2
  delay(3000);
}
