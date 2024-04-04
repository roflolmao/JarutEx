#include <Wire.h>

#define RTC_CTRL 0x00
#define RTC_SEC_100 0x01
#define RTC_SEC 0x02
#define ALM_CTRL 0x08
#define RTC_YEAR_MEM_ADDR 0x20
#define RTC_BEGIN_YEAR 2020

uint8_t dec2bcd(uint8_t n) { 
// แปลงเลขฐาน 10 เป็นรหัส BCD
  return (((uint8_t)(n / 10) * 16) + (n % 10));
}

uint8_t bcd2dec(uint8_t n) {
// แปลงรหัส BCD เป็นตัวเลขฐาน 10
  return (((uint8_t)(n / 16) * 10) + (n % 16)); 
}

char dayOfWeek[][4] = {"sun", "mon", "tue", "wed", "thu", "fri", "sat"};

class PCF8583 {
  private:
    uint8_t addr;
    uint8_t rtc[8];
    uint16_t beginYear;
  public:
    PCF8583(uint8_t _addr = 81) {
      addr = _addr;
      beginYear = RTC_BEGIN_YEAR;
    }
    void _write(uint8_t ctrl, uint8_t value) {
      Wire.beginTransmission( addr );
      Wire.write( ctrl );
      Wire.write( value );
      Wire.endTransmission();

    }
    void begin() {
      _write(RTC_CTRL, 0x00);
      _write(ALM_CTRL, 0x00);
      // บันทึกค่าปีเริ่มต้นในหน่วยความจำ
      _write(RTC_YEAR_MEM_ADDR, (uint8_t)(beginYear & 0x00FF));
      _write(RTC_YEAR_MEM_ADDR + 1, (uint8_t)(beginYear >> 8));
    }

    bool found() {
      Wire.beginTransmission( addr );
      if (Wire.endTransmission() == 0) {
        return true;
      }
      return false;
    }

    void now() {
      uint8_t buff[5];
      int idx = 0;

      Wire.beginTransmission( addr );
      Wire.write( RTC_YEAR_MEM_ADDR );
      Wire.endTransmission();
      // อ่านค่าปีที่เก็บไว้
      Wire.requestFrom(addr, 2);
      idx = 0;
      while (Wire.available()) {
        buff[idx] = Wire.read();
        idx++;
      }
      beginYear = buff[1] << 8;
      beginYear += buff[0];
      // อ่านข้อมูลจาก PCF8583
      Wire.beginTransmission( addr );
      Wire.write( RTC_SEC );
      Wire.endTransmission();
      Wire.requestFrom(addr, 5);
      idx = 0;
      while (Wire.available()) {  // slave may send less than requested
        buff[idx] = Wire.read();    // receive a byte as character
        idx++;
      }
      // แปลงข้อมูลมาเก็บไว้ในตัวแปร rtc
      rtc[0] = bcd2dec(buff[0]); // second
      rtc[1] = bcd2dec(buff[1]); // minute
      rtc[2] = bcd2dec(buff[2]); // hour
      rtc[3] = bcd2dec(buff[3] & 0x3f); // day
      rtc[4] = bcd2dec(buff[4] & 0x1f); // month
      rtc[5] = (buff[3] >> 6); // year
      rtc[6] = buff[4] >> 5; // day of week
    }

    void show() {
      Serial.print(dayOfWeek[rtc[6]]);
      Serial.print(". ");
      Serial.print(rtc[3]);
      Serial.print("/");
      Serial.print(rtc[4]);
      Serial.print("/");
      Serial.print(rtc[5]+beginYear);
      Serial.print(" ");
      Serial.print(rtc[2]);
      Serial.print(":");
      Serial.print(rtc[1]);
      Serial.print(":");
      Serial.print(rtc[0]);
      Serial.println(" ");
    }

    void adjust(uint8_t day, uint8_t month, uint16_t year,
    uint8_t dow, 
    uint8_t hour, uint8_t minute, uint8_t second) {
      uint8_t y = (year-RTC_BEGIN_YEAR)<<6;
      uint8_t d = dow<<5;
      Wire.beginTransmission( addr );
      Wire.write( RTC_SEC );
      Wire.write( dec2bcd(second) );
      Wire.write( dec2bcd(minute) );
      Wire.write( dec2bcd(hour) );
      Wire.write( dec2bcd(day)+y );
      Wire.write( dec2bcd(month)+d );
      Wire.endTransmission();
    }
};

PCF8583 rtc;

void setup() {
  Serial.begin(115200);
  Serial.println("\n------------------\n");
  Wire.begin();
  if (rtc.found()) {
    rtc.begin();
    Serial.println("Found PCF8583");
    rtc.adjust(4,7,2021,0,21,20,0); // ตั้งเวลาใหม่ (อย่าลืมเปลี่ยนนะครับ)
  } else {
    Serial.println("Not found PCF8583");
    while(true);
  }
}

void loop() {
  rtc.now();
  rtc.show();
  delay(1000);
}
