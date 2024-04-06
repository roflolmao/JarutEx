#define ST7735_DRIVER 

#define TFT_RGB_ORDER TFT_BGR
#define TFT_WIDTH  80
#define TFT_HEIGHT 160

#define ST7735_GREENTAB160x80   // For 160 x 80 display with 24 pixel offset

#define TFT_MISO -1 // 37
#define TFT_MOSI 35
#define TFT_SCLK 36
#define TFT_CS   34  // Chip select control pin
#define TFT_DC   33  // Data Command control pin
#define TFT_RST  38  // Reset pin (could connect to Arduino RESET pin)

#define LOAD_GLCD 
#define LOAD_FONT2
#define LOAD_FONT4
#define LOAD_FONT6
#define LOAD_FONT7
#define LOAD_FONT8
#define LOAD_GFXFF  
#define SMOOTH_FONT
#define SPI_FREQUENCY  27000000
