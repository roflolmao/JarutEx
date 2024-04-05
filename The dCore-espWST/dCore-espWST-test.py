##################################################################################
# dCore-espWST-test
# (C) 2021, JarutEx
##################################################################################
import gc
import os
import sys
import time
import math
import machine as mc
from machine import Pin,I2C,ADC
import ssd1306
import dht

##################################################################################
gc.enable()
gc.collect()
mc.freq(160000000)

sclPin = Pin(5)
sdaPin = Pin(4)
dValue = ADC(0)
dht11 = dht.DHT11(Pin(13))
sw = Pin(12, Pin.IN, Pin.PULL_UP)
i2c = I2C(scl=sclPin, sda=sdaPin, freq=1000000)

oled_addr = const(0x3c)
oled = ssd1306.SSD1306_I2C(128,64,i2c,oled_addr)
oled.poweron()
t0 = time.ticks_ms()
t1 = time.ticks_ms()

##################################################################################
def showData():
    global t0,t1
    oled.fill(0)
    oled.fill_rect(0,0,128,18,1)
    oled.text("dCore",8,4,0)
    oled.text("dCore",9,4,0)
    oled.text("espWST1",64,4,0)
    oled.text("LDR :{}".format(dValue.read()),12,28,1)
    t1 = time.ticks_ms()
    if (math.fabs(t0-t1)>2000):
        dht11.measure()
        t0 = time.ticks_ms()
        oled.text("Tem.:{}C".format(dht11.temperature()),12,36,1)
        oled.text("Hum.:{}%".format(dht11.humidity()),12,44,1)
    else:
        oled.text("Tem.:n/a",12,36,1)
        oled.text("Hum.:n/a",12,44,1)
    oled.show()

##################################################################################
# main program
##################################################################################
try:
    oldSwValue = 1
    showData()
    while True:
        swValue = sw.value()
        if ((swValue==0) and (oldSwValue != swValue)):
            showData()
        oldSwValue = swValue
        time.sleep_ms(25) # ป้องกันการกระเพื่อมของสัญญาณจากสวิตช์ (debounce)
except KeyboardInterrupt:
    pass
oled.poweroff()
print("end of program")
