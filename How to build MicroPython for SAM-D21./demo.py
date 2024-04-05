##################################################################################
import gc
import os
import sys
import time
import machine as mc

gc.enable()
gc.collect()

stat = os.statvfs('/flash')
block_size = stat[0]
total_blocks = stat[2]
free_blocks  = stat[3]
rom_total = (total_blocks * block_size)
rom_free = (free_blocks * block_size)
rom_usage = (rom_total-rom_free)

print("Platform .......: {}".format(sys.platform))
print("Frequency ......: {}".format(mc.freq()))
print("ID .............: {}".format(mc.unique_id()))
print("Memoey")
print("    Total ......: {} bytes".format(gc.mem_alloc()+gc.mem_free()))
print("    Used .......: {} bytes".format(gc.mem_alloc()))
print("    Free .......: {} bytes".format(gc.mem_free()))
print("Flash ROM")
print("    Total ......: {} bytes".format(rom_total))
print("    Used .......: {} bytes".format(rom_usage))
print("    Free .......: {} bytes".format(rom_free))
