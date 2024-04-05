###################################################################
### GamePad
# (C) 2021, JarutEx
###################################################################
from machine import Pin, ADC, Timer, SPI
from keypad import Keypad
import time
import gc
import network as nw
import socket
import machine

###################################################################
### system setting
###################################################################
gc.enable()
gc.collect()
machine.freq(240000000)
keypad = Keypad()
tmSwitch = Timer(0) # คุมการรับข้อมูลจากสวิตช์
ssid = 'dCoreMiniML'
passwd = '_miniML_dCore_'
serverIP = '192.168.4.1'
serverPort = 1592
# WiFi
print("Start WiFi")
sta = nw.WLAN( nw.STA_IF )
sta.active(False)
sta.active(True)
# เชื่อมต่อ
sta.connect(ssid, passwd)
while not sta.isconnected():
    time.sleep_ms(200)
print(sta.ifconfig())
serverInfo = socket.getaddrinfo( serverIP, serverPort, 0, socket.SOCK_STREAM )[0]
print("Server info : {}".format(serverInfo))

###################################################################
### Speaker
###################################################################
pinSpk = Pin(25,Pin.OUT)

def beep():
    pinSpk.value(0) # on
    time.sleep_ms(100)
    pinSpk.value(1) # off

def spkOff():
    pinSpk.value(1) # off

spkOff()
beep()

###################################################################
## doInput()
###################################################################
def doInput(x):
    #keypad.show()
    keypad.read()
    status = keypad.status()
    data = bytearray([(status & 0xff00) >> 8,status&0x00ff])
    print(status, data)
    s.write(bytearray(data))

###################################################################
### Main program
###################################################################
# start program
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.connect((serverIP,serverPort))
tmSwitch.init(period=30, mode=Timer.PERIODIC, callback=doInput)
# main loop
try:
    while True:
        time.sleep_ms(10)
except KeyboardInterrupt:
    pass
# end program
tmSwitch.deinit()
sta.disconnect()
sta.active(False)
s.close()
