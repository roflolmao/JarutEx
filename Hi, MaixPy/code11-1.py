# code11-1, By: JarutEx - Fri Oct 16 2020

import sensor, image, time, lcd, os, sys, gc
from machine import I2C
import machine as mc
import Maix

i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29)
uname = os.uname()

mem_total = gc.mem_alloc()+gc.mem_free()
free_percent = str((gc.mem_free())/mem_total*100.0)+"%"
alloc_percent = str((gc.mem_alloc())/mem_total*100.0)+"%"
print("ID .............: {}".format(mc.unique_id()))
print("Platform .......: {}".format(sys.platform))
print("Version ........: {}".format(sys.version))
print("Memory")
print("   total .......: {} Bytes or {} MBytes".format(mem_total, mem_total/(1024*1024)))
print("   usage .......: {} Bytes or {}".format(gc.mem_alloc(),alloc_percent))
print("   free ........: {} Bytes or {}".format(gc.mem_free(),free_percent))
print("system name ....: {}".format(uname.sysname))
print("node name ......: {}".format(uname.nodename))
print("release ........: {}".format(uname.release))
print("version ........: {}".format(uname.version))
print("machine ........: {}".format(uname.machine))
print("CPU Frequency ..: {} MHz".format(Maix.freq.get()[0]))
print("KPU Frequency ..: {} MHz".format(Maix.freq.get()[1]))
if i2c != None:
    devices = i2c.scan()
    i2c_dev = {32:'PCF8574',33:'PCF8574',34:'PCF8574',35:'PCF8574',36:'PCF8574',37:'PCF8574',38:'PCF8574',39:'LCD',56:'LCD',57:'PCF8574',58:'PCF8574',59:'PCF8574',60:'PCF8574/OLED',61:'PCF8574',62:'PCF8574',63:'PCF8574',68:'SHT31', 84:'24xx #1',85:'24xx #2',86:'24xx #3',87:'24xx #4',104:'RTC'}
    if len(devices)==0:
        print("No I2C")
    for io in devices:
        if io in i2c_dev:
            print("Address [",hex(io),"] Device :",i2c_dev[io])
        else:
            print("Address [",hex(io),"] Device : ???")

lcd.init(freq=15000000)
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

img = sensor.snapshot()
lcd.display(img)
sensor.shutdown(0)
