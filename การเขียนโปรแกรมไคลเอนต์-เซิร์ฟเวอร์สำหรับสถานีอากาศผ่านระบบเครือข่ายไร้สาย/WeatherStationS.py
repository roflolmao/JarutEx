#############################################################
# WeatherStationS.py
# สำหรับเครื่องให้บริการ
# (C) 2021, JarutEx
#############################################################
from machine import Pin,I2C,ADC
import dht
import machine
import gc
import time
import os
import sys
import machine as mc
import network as nw
import ubinascii as ua
import socket
import ssd1306
#############################################################
# system
gc.enable()
gc.collect()
machine.freq(240000000)

i2c = I2C(0,scl=Pin(4), sda=Pin(5), freq=100000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

###########################################################
# Sensor
dht22 = dht.DHT22(Pin(15))
ldr = ADC(Pin(39))
ldr.width( ADC.WIDTH_12BIT ) # 12bit
ldr.atten( ADC.ATTN_11DB ) # 3.3V

###########################################################
# Main program
APif = nw.WLAN(nw.AP_IF)
# Set WiFi access point name (formally known as ESSID) and WiFi channel
APif.config(essid='JarutEx_WS',
            password='123456789',
            authmode=nw.AUTH_WPA2_PSK,
            channel=1, hidden=True)
APif.active(True)

def showInfo():
    # shiw IPAddress
    display.fill(0)
    display.text("--AP Config.--",0,0,1)
    display.text("{}".format(APif.ifconfig()[0]), 0, 8, 1)
    display.text("{}".format(APif.config('essid')), 0, 16, 1)
    display.show()

showInfo()
# main loop
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
s.bind(('',3002))
s.listen(5)
try:
    while True:
        conn, addr = s.accept()
        request = conn.recv(1024)
        if (request == b'tem'):
            dht22.measure()
            conn.send("{}".format(dht22.temperature()))
        elif (request == b'hum'):
            dht22.measure()
            conn.send("{}".format(dht22.humidity()))
        elif (request == b'ldr'):
            conn.send("{}".format(ldr.read()))
        else:
            conn.send("na")
        conn.close()
except KeyboardInterrupt:
    pass
s.close()
# end of program
APif.active(False)
