#
# dht11stat.py
# 2021, JarutEx
# https://www.jarutex.com
#
import network as nw
from machine import Pin
import dht
import time
from machine import Timer
from jQueue import Queue
import socket

#set up
maxData = const(20)
dht11PinNo = const(23)
ssid = 'JarutEx-AP'
password = '123456789'
storage = Queue(maxData)
for i in range(maxData):
    storage.push([0,0])

def getDHT11(x):
    dht11.measure()
    tem = dht11.temperature()
    hum = dht11.humidity()
    #print("{}. T: {}C H: {}%".format(i, tem,hum))
    storage.pop()
    storage.push([tem,hum])

if __name__=='__main__':
    dht11 = dht.DHT11(Pin(dht11PinNo))
    dht11Timer = Timer( 0 )
    dht11Timer.init( period=5000, mode=Timer.PERIODIC, callback=getDHT11 )
    ap = nw.WLAN(nw.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)
    while ap.active() == False:
        pass
    print("AP configuration\n{}".format(ap.ifconfig()))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print('conn {} from {}'.format(conn, addr))
        request = conn.recv(1024)
        print('request = {}'.format(request))
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.send("""<html><head><meta name="viewport"
          content="width=device-width, initial-scale=1">
          <meta charset="utf-8">
          </head>
          <body><div><h1>DHT11</h1>
            <canvas id="myCanvas" width="200" height="200" style="border:1px solid #000000;"></canvas>
            </div>
            <script>
                var canvas = document.getElementById("myCanvas");
                var ctx = canvas.getContext("2d");
            """)
        for i in range(maxData):
            conn.send("""
                ctx.fillStyle = "#AA0000";
                ctx.fillRect(0,
                """)
            conn.send(str(i*10))
            conn.send(",")
            conn.send(str(storage.items[i][0]*2))
            conn.send(",4);")
            conn.send("""
                ctx.fillStyle = "#000099";
                ctx.fillRect(0,
                """)
            conn.send(str(i*10+4))
            conn.send(",")
            conn.send(str(storage.items[i][1]*2))
            conn.send(",4);")
        conn.send("</script></body></html>")
        conn.close()
