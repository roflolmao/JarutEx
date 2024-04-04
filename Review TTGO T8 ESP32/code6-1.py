# code6-1
# (C) 2020, JarutEx
import esp
import esp32
import os
import sys
import machine as mc
import gc
import time
gc.enable()
gc.collect()
uname = os.uname()
mem_total = gc.mem_alloc()+gc.mem_free()
free_percent = str((gc.mem_free())/mem_total*100.0)+"%"
alloc_percent = str((gc.mem_alloc())/mem_total*100.0)+"%"
print("ID ............: {}".format(mc.unique_id()))
print("Platform ......: {}".format(sys.platform))
print("Version .......: {}".format(sys.version))
print("ROM Size ......: {} MBytes".format(esp.flash_size()/(1024*1024)))
print("Memory")
print("   total ......: {} Bytes or {} MBytes".format(mem_total, mem_total/(1024*1024)))
print("   usage ......: {} Bytes or {}".format( gc.mem_alloc(), alloc_percent))
print("   free .......: {} Bytes or {}".format( gc.mem_free(), free_percent))
print("system name ...: {}".format(uname.sysname))
print("node name .....: {}".format(uname.nodename))
print("release .......: {}".format(uname.release))
print("version .......: {}".format(uname.version))
print("machine .......: {}".format(uname.machine))
print("Frequency .....: {} MHz".format(mc.freq()/1000000.0))
print("Temperature ...: {}F".format(esp32.raw_temperature()))
print("Hall ..........: {}".format(esp32.hall_sensor()))
