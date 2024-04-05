#############################################
# SaveDHT2File.py
# (C) 2021, JarutEx
# 2021-09-15
#############################################
import os
import dht
from machine import Pin

dht22 = dht.DHT22(Pin(15))
filename = 'dht22log.txt'
if (filename in os.listdir()):
    f = open(filename,'a')
else:
    f = open(filename,'w')
dht22.measure()
print("Write...")
f.write("Temperature ....: {}C, Humidity .......: {}%\n".format(
    dht22.temperature(),
    dht22.humidity())
)
f.close()
print("Read...")
f = open(filename,'r')
print(f.read())
f.close()
