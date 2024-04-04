#code4-2
import socket
import network
import esp
from machine import ADC
#---(1)
pinAdc = ADC(0)
ap = network.WLAN(network.AP_IF)
#---(2)
ssid = 'JarutEx-AP'
password = '123456789'
ap.active(True)
ap.config(essid=ssid, password=password)
while ap.active() == False:
  pass
print('Connection successful')
#---(3)
def web_page():
    dValue = pinAdc.read()
    html = """<html><head><meta name="viewport"
      content="width=device-width, initial-scale=1"></head>
      <body><h1>Sensor Value = """
    html += str(dValue)
    html += "</h1></body></html>"
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
    request = conn.recv(1024)
    print('request = {}'.format(request))
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.send(response)
    conn.close()
