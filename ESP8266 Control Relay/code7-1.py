# code7-1 relay
# D1 --> Relay (S)
import socket
import network
import esp
import time
import gc
from machine import Pin
from machine import ADC
#---(1)
gc.collect()
relayPin = Pin(5,Pin.OUT) # D1
ap = network.WLAN(network.AP_IF)
#---(2)
ssid = 'JarutEx-AP'
password = '123456789'
relayState = False
ap.active(True)
ap.config(essid=ssid, password=password)
while ap.active() == False:
  pass
print('Connection successful')
#---(3)
def ledOn():
    global relayState
    relayPin.value(1)
    relayState = True
def ledOff():
    global relayState
    relayPin.value(0)
    relayState = False
def web_page():
    global relayState
    html = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>.button {  border: none;  color: white;  padding: 20px;  text-align: center;  text-decoration: none;
  display: inline-block;  font-size: 16px;  margin: 4px 2px;  cursor: pointer;  border-radius: 52%;
}
.button1 {  background-color: #3ABC40; }
.button2 {  background-color: #BC4040; }
</style></head><body>
"""
    if relayState == False:
        html += "<a href='/?relay=on'><button  class='button button1'>On</button></a>"
    else:
        html += "<a href='/?relay=off'><button class='button button2'>Off</button></a>"
    html += "</body></html>"
    return html
#---(4)
print(ap.ifconfig())
#---(5)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
#---(6)
while True:
    conn, addr = s.accept()
    print('conn {} from {}'.format(conn, addr))
    request = str(conn.recv(1024))
    print('request = {}'.format(request))
    relay_on = request.find('/?relay=on')
    relay_off = request.find('/?relay=off')
    if relay_on == 6:
        ledOn()
    if relay_off == 6:
        ledOff()
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.send(response)
    conn.close()
