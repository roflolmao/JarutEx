#############################################################
# WeatherStationC.py
# สำหรับเครื่องให้บริการ
# (C) 2021, JarutEx
#############################################################
import machine
import gc
import time
import os
import sys
import network as nw
import ubinascii as ua
import socket

#############################################################
# system
gc.enable()
gc.collect()
machine.freq(240000000)

###########################################################
# Main program
sta = nw.WLAN( nw.STA_IF )
sta.active(True)
# เชื่อมต่อ
sta.connect('JarutEx_WS','123456789')
while not sta.isconnected():
    time.sleep_ms(200)
print(sta.ifconfig())
serverInfo = socket.getaddrinfo( '192.168.4.1', 3002, 0, socket.SOCK_STREAM )[0]
print("Server info : {}".format(serverInfo))
# ร้องขอค่าอุณหภูมิ
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.connect(serverInfo[-1])
s.write(b'tem')
result = s.readline()
s.close()
print("Temperature : {}C".format(result))
# ร้องขอค่าความชื้น
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.connect(serverInfo[-1])
s.write(b'hum')
result = s.readline()
s.close()
print("Humidity : {}%".format(result))
# ร้องขอค่าจาก LDR
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.connect(serverInfo[-1])
s.write(b'ldr')
result = s.readline()
print("LDR Value : {}".format(result))
s.close()


###########################################################
# End of Program
sta.active(False)
