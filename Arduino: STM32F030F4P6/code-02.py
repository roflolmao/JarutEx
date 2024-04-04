#code-02 โค้ดของ ESP8266
from machine import Pin, I2C
import time

sclPin = Pin(5)
sdaPin = Pin(4)
devAddr = const(0x17)
devLedAddr = const(0x00)
devSpkAddr = const(0x01)
devBuffer = bytearray(2)

i2c = I2C(sda = sdaPin, scl = sclPin )
time.sleep_ms(250)
print("Begin of Program")
print(i2c.scan())
for i in range(10): # blink
    devBuffer[0] = devLedAddr
    devBuffer[1] = 0
    i2c.writeto(devAddr, devBuffer)
    time.sleep_ms(100)
    devBuffer[1] = 1
    i2c.writeto(devAddr, devBuffer)
    time.sleep_ms(100)
print("End of Program")
