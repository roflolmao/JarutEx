# code17-3
import sys
import gc
import os
import time
import dht
import machine as mc
from kjlcd import LCD
sclPin = mc.Pin(5) #D1
sdaPin = mc.Pin(4) #D2
dht22Pin = mc.Pin(2) #D4
i2c = mc.I2C(scl=sclPin,sda=sdaPin)
dht22 = dht.DHT22(dht22Pin)
lcd_addr= const(0x27)
lcd = LCD(i2c,lcd_addr)
tMin = 99.0
tMax = 0.0
hMin = 99.9
hMax = 0.0
while True:
    dht22.measure()
    tempValue = dht22.temperature()
    humidValue = dht22.humidity()
    if (tMin > tempValue):
        tMin = tempValue
    if (tMax < tempValue):
        tMax = tempValue
    if (hMin > humidValue):
        hMin = humidValue
    if (hMax < humidValue):
        hMax = humidValue
    tAverage = tMin + ((tMax-tMin)/2.0)
    hAverage = hMin + ((hMax-hMin)/2.0)
    lcd.goto(0,0)
    lcd.puts("T-Average: {:4.1f}C ".format(tAverage))
    lcd.goto(0,1)
    lcd.puts("H-Average: {:4.1f}% ".format(hAverage))
    time.sleep_ms(1900)
