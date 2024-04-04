# Joystick module + ESP32 + MicroPython
# By JarutEx (https://www.jarutex.com)
from machine import Pin, ADC
import time
import machine as mc
import gc

gc.collect()
gc.enable()

mc.freq(240000000)

vrx = ADC(Pin(36, Pin.IN))
vrx.atten(ADC.ATTN_11DB)       #Full range: 3.3v
vry = ADC(Pin(39, Pin.IN))
vry.atten(ADC.ATTN_11DB)       #Full range: 3.3v

swPins = [
    Pin(2, Pin.IN, Pin.PULL_UP), # A
    Pin(14, Pin.IN, Pin.PULL_UP), # B
    Pin(13, Pin.IN, Pin.PULL_UP), # C
    Pin(15, Pin.IN, Pin.PULL_UP), # D
    Pin(16, Pin.IN, Pin.PULL_UP), # E
    Pin(26, Pin.IN, Pin.PULL_UP) #f
]

vrxValue = 0
vryValue = 0
swValue = [1,1,1,1,1,1]

def doUpdate():
    global vrxValue, vryValue, swValue
    vrxValue = vrx.read()
    vryValue = vry.read()
    for i in range(6):
        swValue[i] = swPins[i].value() 
    
def doShow():
    print("({},{}):A{}/B{}/C{}/D{}/E{}/F{}".format(
        vrxValue,vryValue,
        swValue[0],swValue[1],swValue[2],
        swValue[3],swValue[4],swValue[5]))

while True:
    doUpdate()
    doShow()
    time.sleep_ms(200)
