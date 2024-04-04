#define U8G2_WITH_UNICODE
#include <Arduino.h>
#include <U8g2lib.h>

//U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);
U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);

void setup(void) {
  u8g2.begin();
}

void loop(void) {
  u8g2.firstPage();
  do {
  u8g2.setFont(u8g2_font_etl14thai_t ); 
  u8g2.drawUTF8(8,37, "สวัสดี");  
  } while ( u8g2.nextPage() );
  delay(1000);
 }
