#define ST7735_DRIVER 

#define TFT_RGB_ORDER TFT_RGB 
#define TFT_WIDTH  80
#define TFT_HEIGHT 160

#define ST7735_REDTAB160x80   // For 160 x 80 display with 24 pixel offset

#define TFT_INVERSION_ON

// ESP32-S2
#define TFT_MISO -1 // 37
#define TFT_MOSI 35
#define TFT_SCLK 36
#define TFT_CS   34  // Chip select control pin
#define TFT_DC   33  // Data Command control pin
#define TFT_RST  38  // Reset pin (could connect to Arduino RESET pin)

#define LOAD_GLCD   // Font 1. Original Adafruit 8 pixel font needs ~1820 bytes in FLASH
#define LOAD_FONT2  // Font 2. Small 16 pixel high font, needs ~3534 bytes in FLASH, 96 characters
#define LOAD_FONT4  // Font 4. Medium 26 pixel high font, needs ~5848 bytes in FLASH, 96 characters
#define LOAD_FONT6  // Font 6. Large 48 pixel font, needs ~2666 bytes in FLASH, only characters 1234567890:-.apm
#define LOAD_FONT7  // Font 7. 7 segment 48 pixel font, needs ~2438 bytes in FLASH, only characters 1234567890:-.
#define LOAD_FONT8  // Font 8. Large 75 pixel font needs ~3256 bytes in FLASH, only characters 1234567890:-.
//#define LOAD_FONT8N // Font 8. Alternative to Font 8 above, slightly narrower, so 3 digits fit a 160 pixel TFT
#define LOAD_GFXFF  // FreeFonts. Include access to the 48 Adafruit_GFX free fonts FF1 to FF48 and custom fonts

#define SMOOTH_FONT

#define SPI_FREQUENCY  27000000
