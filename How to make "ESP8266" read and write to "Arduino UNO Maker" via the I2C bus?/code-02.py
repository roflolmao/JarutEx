from machine import Pin, I2C
import time

sclPin = Pin(5)
sdaPin = Pin(4)
unoAddr = 7
unoBuffer = bytearray(2)

i2c = I2C(sda = sdaPin, scl = sclPin, freq=100000)
unoBuffer[0] = 0
unoBuffer[1] = 0
i2c.writeto(unoAddr, unoBuffer)
time.sleep_ms(1000)
unoBuffer[0] = 1
unoBuffer[1] = 0
i2c.writeto(unoAddr, unoBuffer)
time.sleep_ms(1000)
unoBuffer[0] = 2
unoBuffer[1] = 0xAA;
i2c.writeto(unoAddr, unoBuffer)
time.sleep_ms(1000)
dInput = i2c.readfrom(unoAddr,1)
print(dInput)
