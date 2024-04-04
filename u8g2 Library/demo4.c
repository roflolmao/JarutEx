#define U8G2_WITH_UNICODE
#include <Arduino.h>
#include <U8g2lib.h>

U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);
//U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);

void setup(void) {
  u8g2.begin();
}

void loop(void) {
  u8g2.firstPage();
  do {
    u8g2.setFont(u8g2_font_6x10_tf);
    u8g2.setFontRefHeightAll();    /* this will add some extra space for the text inside the buttons */
    u8g2.userInterfaceMessage("Title1", "Title2", "Title3", " Ok \n Cancel ");
  } while ( u8g2.nextPage() );
  delay(1000);
}
