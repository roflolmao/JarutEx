# dhtBar.py
from machine import Pin,I2C
import dht
import machine
import gc
import ssd1306
import time

# system
gc.enable()
gc.collect()
machine.freq(240000000)

# OLED
sclPin = Pin(4)
sdaPin = Pin(5)
i2c = I2C(0,scl=sclPin,sda=sdaPin)
oled = ssd1306.SSD1306_I2C(128,32,i2c)
oled.poweron()
oled.contrast(255)
oled.init_display()
oled.fill(0)
oled.text("JarutEx", 40, 24)
for i in range(32):
    oled.show()
    oled.scroll(0,-1)
    time.sleep_ms(30)

# Sensor
dht22 = dht.DHT22(Pin(15))

# main program
barWidth = 88
barHeight = 6
maxTem = 40.0
maxHum = 100.0
bT0 = True

while True:
    dht22.measure()
    tem = dht22.temperature()
    hum = dht22.humidity()
    if (bT0): # 1st time ให้เอนิเมทกราฟ
        bT0 = False
        x1 = int(barWidth*tem/maxTem)
        x2 = 0
        xAnim = 0
        while (xAnim <= x1):
            oled.fill(0)
            oled.text("T={}C".format(tem), 10, 0)
            oled.text("0",0,8)
            oled.text("{}".format(int(maxTem)),100,8)
            oled.text("H={}%".format(hum), 10, 16)
            oled.text("0",0,24)
            oled.text("{}".format(int(maxHum)),100,24)
            for x in range(barWidth):
                oled.pixel(10+x,10,1)
                oled.pixel(10+x,26,1)
            for y in range(barHeight):
                oled.pixel(xAnim-1,8+y,1)
                oled.pixel(x2-1,24+y,1)
                oled.pixel(xAnim,8+y,1)
                oled.pixel(x2,24+y,1)
                oled.pixel(xAnim+1,8+y,1)
                oled.pixel(x2+1,24+y,1)
            oled.show()
            xAnim += 1
        x2 = int(barWidth*hum/maxHum)
        xAnim = 0
        while (xAnim <= x2):
            oled.fill(0)
            oled.text("T={}C".format(tem), 10, 0)
            oled.text("0",0,8)
            oled.text("{}".format(int(maxTem)),100,8)
            oled.text("H={}%".format(hum), 10, 16)
            oled.text("0",0,24)
            oled.text("{}".format(int(maxHum)),100,24)
            for x in range(barWidth):
                oled.pixel(10+x,10,1)
                oled.pixel(10+x,26,1)
            for y in range(barHeight):
                oled.pixel(x1-1,8+y,1)
                oled.pixel(xAnim-1,24+y,1)
                oled.pixel(x1,8+y,1)
                oled.pixel(xAnim,24+y,1)
                oled.pixel(x1+1,8+y,1)
                oled.pixel(xAnim+1,24+y,1)
            oled.show()
            xAnim += 1
    else:
        oled.fill(0)
        oled.text("T={}C".format(tem), 10, 0)
        oled.text("0",0,8)
        oled.text("{}".format(int(maxTem)),100,8)
        oled.text("H={}%".format(hum), 10, 16)
        oled.text("0",0,24)
        oled.text("{}".format(int(maxHum)),100,24)
        for x in range(barWidth):
            oled.pixel(10+x,10,1)
            oled.pixel(10+x,26,1)
        x1 = int(barWidth*tem/maxTem)
        x2 = int(barWidth*hum/maxHum)
        for y in range(barHeight):
            oled.pixel(x1-1,8+y,1)
            oled.pixel(x2-1,24+y,1)
            oled.pixel(x1,8+y,1)
            oled.pixel(x2,24+y,1)
            oled.pixel(x1+1,8+y,1)
            oled.pixel(x2+1,24+y,1)
        oled.show()
        time.sleep_ms(10000)
