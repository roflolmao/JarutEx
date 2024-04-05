#############################################################
#GameDisplay.py
# สำหรับเครื่องให้บริการ
# (C) 2021, JarutEx
#############################################################
from machine import Pin,SPI,SDCard,ADC
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
from st7735x import TFT
#############################################################
# system
gc.enable()
gc.collect()
machine.freq(240000000)

ssid = 'dCoreMiniML'
passwd = '_miniML_dCore_'
serverIP = '192.168.4.1'
serverPort = 1592

class coreDisplay:
    def __init__(self):
        self.spi = None
        self.dev = None
        self.use()
        self.unused()
    
    def use(self):
        self.spi = SPI(2, baudrate=33000000,
          sck=Pin(14), mosi=Pin(12),
          polarity=0, phase=0)
        # dc, rst, cs
        self.dev=TFT(self.spi,15,13,2)
    
    def unused(self):
        self.spi.deinit() # ปิด


tft = coreDisplay()
tft.use()

########################################
## เปิดใช้งาน TFT

tft.dev.fill(tft.dev.BLACK)
tft.dev.text("(C)2020-21",(10,24),tft.dev.YELLOW)
tft.dev.text("JarutEx",(92,244),tft.dev.WHITE)
tft.dev.text("JarutEx",(93,24),tft.dev.WHITE)
tft.dev.swap()

###########################################################
# Main program
APif = nw.WLAN(nw.AP_IF)
# Set WiFi access point name (formally known as ESSID) and WiFi channel
APif.config(essid=ssid,
            password=passwd,
            authmode=nw.AUTH_WPA2_PSK,
            channel=1, hidden=True)
APif.active(True)
print(APif.ifconfig())

# main loop
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
s.bind(('',serverPort))
s.listen(1)
conn, addr = s.accept()

pos = [78,38]
tft.dev.fill(tft.dev.BLACK)
tft.dev.fillrect(pos,(4,4),tft.dev.RED)
tft.dev.swap()

try:
    while True:
        request = (int).from_bytes(conn.recv(2),'big')
        print(request)
        if (request & 0x0400): # left 1024
            pos[0] -= 1
        if (request & 0x0200): # right 512
            pos[0] += 1
        if (request & 0x0080): # up 128
            pos[1] -= 1
        if (request & 0x0040): # down 64
            pos[1] += 1
        tft.dev.fill(tft.dev.BLACK)
        tft.dev.fillrect(pos,(4,4),tft.dev.RED)
        tft.dev.swap()
except KeyboardInterrupt:
    pass
conn.close()
s.close()
APif.active(False)
