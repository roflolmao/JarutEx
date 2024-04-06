#include <Arduino.h>
#include <SPI.h>
#include <TFT_eSPI.h>

TFT_eSPI tft = TFT_eSPI();

void setup() {
  char msg[64];
  tft.init();
  tft.setRotation(1);
  
  tft.fillScreen( TFT_MAROON );
  tft.setTextColor( TFT_CYAN );
  tft.drawString("HEAP info.",4,0,2);

  sprintf(msg,"%.2f/%.2fKB", ESP.getFreeHeap()/1024.0, ESP.getHeapSize()/1024.0);
  tft.setTextColor( TFT_WHITE );
  tft.drawString( msg, 12 , 12,  2  );

  tft.setTextColor( TFT_CYAN );
  tft.drawString("PSRAM info.",4,32,2);

  sprintf(msg,"%.2f/%.2fMB", ESP.getFreePsram()/1048576.0, ESP.getPsramSize()/1048576.0);
  tft.setTextColor( TFT_WHITE );
  tft.drawString( msg, 12 , 44,  2  );

  tft.setTextColor( TFT_YELLOW );
  tft.drawString("www.jarutex.com",22,60,2);
}

void loop() {

}
