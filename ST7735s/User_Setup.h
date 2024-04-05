#define ST7735_DRIVER


#define TFT_WIDTH  80
#define TFT_HEIGHT 160


#define ST7735_REDTAB160x80
#define TFT_INVERSION_ON

#define TFT_MISO PA6
#define TFT_MOSI PA7
#define TFT_SCLK PA5
#define TFT_CS   PB1  
#define TFT_DC   PB0  
#define TFT_RST  -1  

#define LOAD_GLCD   // Font 1. Original Adafruit 8 pixel font needs ~1820 bytes in FLASH
#define LOAD_FONT2  // Font 2. Small 16 pixel high font, needs ~3534 bytes in FLASH, 96 characters

#define SMOOTH_FONT


#define SPI_FREQUENCY  27000000 
