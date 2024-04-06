#include <Arduino.h>
#include <SPI.h>
#include <TFT_eSPI.h>

TFT_eSPI tft = TFT_eSPI();

void setup() {
  char msg[64];
  tft.init();
  tft.setRotation(1);
  tft.writecommand(TFT_MADCTL);
  tft.writedata(TFT_MAD_MV | TFT_MAD_COLOR_ORDER );
  tft.fillScreen( TFT_MAROON );

  sprintf(msg,"Total heap: %d", ESP.getHeapSize());
  tft.setTextColor( TFT_WHITE );
  tft.drawString( msg, 4 , 0,  2  );
  
  sprintf(msg,"Free heap: %d", ESP.getFreeHeap());
  tft.setTextColor( TFT_CYAN );
  tft.drawString( msg, 4 , 12,  2  );

  sprintf(msg,"Total PSRAM: %d", ESP.getPsramSize());
  tft.setTextColor( TFT_WHITE );
  tft.drawString( msg, 4 , 24,  2  );

  sprintf(msg,"Free PSRAM: %d", ESP.getFreePsram());
  tft.setTextColor( TFT_CYAN );
  tft.drawString( msg, 4 , 36,  2  );

  tft.setTextColor( TFT_YELLOW );
  tft.drawString("www.jarutex.com",4,60,2);
}

void loop() {
  // put your main code here, to run repeatedly:

}
