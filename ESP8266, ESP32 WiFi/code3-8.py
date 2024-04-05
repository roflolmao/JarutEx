#code3-8
import esp
import time
import socket
import network
from machine import Pin, I2C

sclPin = Pin(5)
sdaPin = Pin(4)
unoAddr = 7
unoBuffer = bytearray(2)
unoStatus = 0
i2c = I2C(sda = sdaPin, scl = sclPin, freq=100000)

ap = network.WLAN(network.AP_IF)
ssid = 'JarutEx-AP'
password = '123456789'
ap.active(True)
ap.config(essid=ssid, password=password)
while ap.active() == False:
  pass
print('Connection successful')

def doOn():
    global unoBuffer
    global unoAddr
    unoBuffer[0] = 1
    unoBuffer[1] = 0
    i2c.writeto(unoAddr, unoBuffer)
    
def doOff():
    global unoBuffer
    global unoAddr
    unoBuffer[0] = 0
    unoBuffer[1] = 0
    i2c.writeto(unoAddr, unoBuffer)
    
def doReadStatus():
    global unoStatus
    global unoAddr
    unoStatus = i2c.readfrom(unoAddr,1)
    
def web_page():
    doReadStatus()
    html = """<html><head><meta name="viewport"
      content="width=device-width, initial-scale=1"></head>
      <body><h1>Status = """
    html += str(unoStatus)
    html += "</h1>"
    html += """<p><a href="/?led=on"><button>ON</button></a></p>
  <p><a href="/?led=off"><button>OFF</button></a></p>"""
    html += "</body></html>"
    return html

print(ap.ifconfig())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('conn {} from {}'.format(conn, addr))
    request = str(conn.recv(1024))
    print('request = {}'.format(request))
    ledOn = request.find("/?led=on")
    ledOff = request.find("/?led=off")
    if (ledOn==6):
        doOn()
    if (ledOff==6):
        doOff()
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')    
    conn.send(response)
    conn.close()
