import os
import sys
import machine as mc
import gc
import time
if sys.platform == 'esp8266':
    import esp
    scl_pin = mc.Pin(5)
    sda_pin = mc.Pin(4)
    i2c = mc.I2C(scl=scl_pin,sda=sda_pin)
else: 
    scl_pin = None
    sda_pin = None
    i2c = None
uname = os.uname()
if sys.platform == 'esp8266':
    mc.freq(160000000)
mem_total = gc.mem_alloc()+gc.mem_free()
free_percent = str((gc.mem_free())/mem_total*100.0)+"%"
alloc_percent = str((gc.mem_alloc())/mem_total*100.0)+"%"
print("ID ............: {}".format(mc.unique_id()))
print("Platform ......: {}".format(sys.platform))
print("Version .......: {}".format(sys.version))
if sys.platform == 'esp8266':
    print("ROM Size ......: {} MBytes".format(esp.flash_size()/(1024*1024)))
print("Memory")
print("   total ......: {} Bytes or {} MBytes".format(mem_total, mem_total/(1024*1024)))
print("   usage ......: {} Bytes or {}".format(gc.mem_alloc(),alloc_percent))
print("   free .......: {} Bytes or {}".format(gc.mem_free(),free_percent))
print("system name ...: {}".format(uname.sysname))
print("node name .....: {}".format(uname.nodename))
print("release .......: {}".format(uname.release))
print("version .......: {}".format(uname.version))
print("machine .......: {}".format(uname.machine))
if sys.platform == 'esp8266':
    print("Frequency .....: {} MHz".format(mc.freq()/1000000.0))
if i2c != None:
    devices = i2c.scan()
    i2c_dev = {32:'PCF8574',33:'PCF8574',34:'PCF8574',35:'PCF8574',36:'PCF8574',37:'PCF8574',38:'PCF8574',39:'LCD',56:'LCD',57:'PCF8574',58:'PCF8574',59:'PCF8574',
               60:'PCF8574/OLED',61:'PCF8574',62:'PCF8574',63:'PCF8574',68:'SHT31', 84:'24xx #1',85:'24xx #2',86:'24xx #3',87:'24xx #4',104:'RTC'}
    if len(devices)==0:
        print("No I2C")
    for io in devices:
        if io in i2c_dev:
            print("Address [",hex(io),"] Device :",i2c_dev[io])
        else:
            print("Address [",hex(io),"] Device : ???")
