# code17-1
import sys
import gc
import os
import time
import dht
import machine as mc
from kjlcd import LCD
sclPin = mc.Pin(5) #D1
sdaPin = mc.Pin(4) #D2
sensorPin = mc.Pin(2) #D4
i2c = mc.I2C(scl=sclPin,sda=sdaPin)
sensor= dht.DHT22(sensorPin)
sensor.measure()
tempValue = sensor.temperature()
humidValue = sensor.humidity()
lcd_addr= const(0x27)
lcd = LCD(i2c,lcd_addr)
lcd.goto(0,0)
lcd.puts("T:{}C H:{}%".format(tempValue, humidValue))
lcd.goto(0,1)
lcd.puts("(C)2020,JarutEx")
