###########################################
## (C) 2021, JarutEx
## https://www.jarutex.com
## https://docs.micropython.org/en/latest/library/machine.I2C.html
###########################################
import machine as mc
import time
SCL_PIN = mc.Pin(5)
SDA_PIN = mc.Pin(4)
i2c = mc.I2C(freq=2000000, scl=SCL_PIN, sda=SDA_PIN)
devices = i2c.scan()

PCF8583_ADDR = 0xA2 >> 1
RTC_CTRL = 0x00;
RTC_SEC_100 = 0x01
RTC_SEC = 0x02
ALM_CTRL = 0x08
RTC_YEAR_MEM_ADDR = 0x20

def int2bytes(x):
    return x.to_bytes(2, 'big')

def bytes2int(x):
    return int.from_bytes(x, 'big')

def dec2bcd(n):
    return ((n // 10 * 16) + (n % 10))

def bcd2dec(n):
    return ((n // 16 * 10) + (n % 16))

RTC_BEGIN_YEAR = 2020

rtc = [0,0,0,0,0,0,0]
dayOfWeek = ["sun","mon","tue","wed","thu","fri","sat"]

def begin():
    i2c.writeto_mem(PCF8583_ADDR,RTC_CTRL, b'\x00')
    i2c.writeto_mem(PCF8583_ADDR,ALM_CTRL, b'\x00')
    beginYear = int2bytes(RTC_BEGIN_YEAR)
    i2c.writeto_mem(PCF8583_ADDR,RTC_YEAR_MEM_ADDR,
                    bytearray([beginYear[0],beginYear[1]]))    


def now():
    buffer = i2c.readfrom_mem(PCF8583_ADDR,RTC_SEC,5)
    i2c.writeto(PCF8583_ADDR,b'\x20') #RTC_YEAR_MEM_ADDR);
    year = i2c.readfrom(PCF8583_ADDR, 2)
    rtc[0] = bcd2dec(buffer[0]) # second
    rtc[1] = bcd2dec(buffer[1]) # minute
    rtc[2] = bcd2dec(buffer[2]) # hour
    rtc[3] = bcd2dec(buffer[3]&0x3f) # day
    rtc[4] = bcd2dec(buffer[4]&0x1f) # month
    rtc[5] = bytes2int(year)+(buffer[3]>>6) # year
    rtc[6] = buffer[4]>>5 # day of week
    
def show():    
    print("{}. {}/{}/{} {}:{}:{}".format(
        dayOfWeek[rtc[6]],
        rtc[3],
        rtc[4],
        rtc[5],
        rtc[2],
        rtc[1],
        rtc[0]
        ))
    
def adjust(day,month,year,dow,hour,minute,second):
    y = (year-RTC_BEGIN_YEAR)<<6
    d = dow << 5
    buffer = bytearray([0,0,0,0,0])
    buffer[0] = dec2bcd(second)
    buffer[1] = dec2bcd(minute)
    buffer[2] = dec2bcd(hour)
    buffer[3] = dec2bcd(day)+y
    buffer[4] = dec2bcd(month)+d
    i2c.writeto_mem(PCF8583_ADDR,RTC_SEC,buffer)

####################### main program ############################
if __name__=="__main__":
    if not (PCF8583_ADDR in devices):
        print("not found PCF8583!!!")
    else:
        begin()
        adjust(9,6,2021,3,13,35,0)
        cnt = 0
        while cnt<10:
            now()
            show()
            time.sleep_ms(1000)
            cnt = cnt+1
