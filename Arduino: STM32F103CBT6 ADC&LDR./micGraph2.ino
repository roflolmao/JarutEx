// micGraph.ino
// JarutEx
#include <TFT_eSPI.h> // Graphics and font library for ST7735 driver chip
#include <SPI.h>
TFT_eSPI tft = TFT_eSPI();  // Invoke library, pins defined in User_Setup.h

#define textColor TFT_WHITE
#define textBgColor 0x3861
#define pinMic PA0
#define ADC_BITS 12

uint16_t dValue;
uint16_t yValue = 0;

void setup() {
  Serial.begin(115200);
  analogReadResolution(ADC_BITS);
  tft.init();
  tft.setRotation(1);
  tft.writecommand(ST7735_MADCTL);
  tft.writedata(TFT_MAD_MV | TFT_MAD_COLOR_ORDER );
  drawScr();
  Serial.println("Started");
}

void drawScr() {
  tft.fillScreen(textBgColor);
  tft.drawLine(0, 40, 75, 40, textColor);
  tft.drawLine(85, 40, 159, 40, textColor);
}

void loop() {
  // อ่านค่า
  dValue = analogRead( pinMic );

  // ลบเส้นเดิม
  tft.drawLine(75, 40, 80, yValue, textBgColor);
  tft.drawLine(80, yValue, 85, 40, textBgColor);

  // แปลง 0..4095 เป็น 0..79
  yValue = (uint16_t)(((float)dValue / 4095.0) * 79.0);

  // วาดเส้นใหม่
  tft.drawLine(75, 40, 80, yValue, textColor);
  tft.drawLine(80, yValue, 85, 40, textColor);

}
