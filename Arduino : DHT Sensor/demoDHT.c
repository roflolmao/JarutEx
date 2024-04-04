////////////////////////////////////////////////////////
// demoDHT
// chip: stm32f103
// board: stm32-station lab
// (C) 2020-2021, JarutEx
/////////////////////////////////////////////////////////
#include <DHT.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);
DHT dht = DHT(PA1, DHT22);

void setup() {
  Serial.begin(115200);
  dht.begin();
  lcd.init();
  lcd.backlight();
}

void loop() {
  float h = dht.readHumidity();
  float tc = dht.readTemperature();
  float tf = dht.readTemperature(true);

  if (isnan(h) || isnan(tc) || isnan(tf)) {
    lcd.setCursor(0, 1);
    lcd.print("DHTsensor Failed");
    return;
  }

  float hic = dht.computeHeatIndex(tc, h, false);
  float hif = dht.computeHeatIndex(tf, h);

  lcd.setCursor(0, 0);
  lcd.print("STM32-StationLab");
  lcd.setCursor(0, 1);
  lcd.print(" www.jarutex.com");
  delay(2000);

  lcd.setCursor(0, 0);
  lcd.print("T:      C      F");
  lcd.setCursor(3, 0);
  lcd.print(tc);
  lcd.setCursor(10, 0);
  lcd.print(tf);
  lcd.setCursor(0, 1);
  lcd.print("Humidity:     % ");
  lcd.setCursor(9, 1);
  lcd.print(h);
  delay(5000);

  lcd.setCursor(0, 0);
  lcd.print("   Heat index   ");
  lcd.setCursor(0, 1);
  lcd.print("T:      C      F");
  lcd.setCursor(3, 1);
  lcd.print(hic);
  lcd.setCursor(10, 1);
  lcd.print(hif);
  delay(5000);
}
