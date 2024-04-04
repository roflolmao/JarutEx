import sys
if sys.platform != 'esp32':
    print("esp32 only!")
    sys.exit(0)
    
import gc
import os
import esp
import esp32
import time
import machine as mc
import ulab

def show_hw_info():
    uname = os.uname()
    mem_total = gc.mem_alloc()+gc.mem_free()
    free_percent = "("+str((gc.mem_free())/mem_total*100.0)+"%)"
    alloc_percent = "("+str((gc.mem_alloc())/mem_total*100.0)+"%)"
    stat = os.statvfs('/flash')
    block_size = stat[0]
    total_blocks = stat[2]
    free_blocks  = stat[3]
    rom_total = (total_blocks * block_size)/1024
    rom_free = (free_blocks * block_size)/1024
    rom_usage = (rom_total-rom_free)
    rfree_percent = "("+str(rom_free/rom_total*100.0)+"%)"
    rusage_percent = "("+str(rom_usage/rom_total*100.0)+"%)"
    print("ID ............:",mc.unique_id())
    print("Platform ......:",sys.platform)
    print("Version .......:",sys.version)
    print("Memory")
    print("   total ......:",mem_total/1024,"KB")
    print("   usage ......:",gc.mem_alloc()/1024,"KB",alloc_percent)
    print("   free .......:",gc.mem_free()/1024,"KB",free_percent)
    print("ROM")
    print("   total ......:", rom_total,"KB" )
    print("   usage ......:", rom_usage,"KB",rfree_percent )
    print("   Free .......:", rom_free,"KB",rusage_percent )
    print("system name ...:",uname.sysname)
    print("node name .....:",uname.nodename)
    print("release .......:",uname.release)
    print("version .......:",uname.version)
    print("machine .......:",uname.machine)

def show_ulab():
    print("ulab version {}.".format(ulab.__version__))

if __name__=="__main__":
    show_hw_info()
    show_ulab()
