##################################################################################
# coreInfo
# esp8266/esp32/rp2/stm32f4/stm32f7/micro:bit information
##################################################################################
import gc
import os
import sys
import time

##################################################################################
# system setting
##################################################################################
gc.enable()
gc.collect()

##################################################################################
# function
##################################################################################
def isPrime(x):
    i = 2
    while (i < x):
        if x%i == 0:
            return False
        i = i+1
    if (i == x):
        return True
    return False

def testPrimeNumber(maxN):
    counter = 0
    t0 = time.monotonic_ns()
    for n in range(2, maxN):
        if isPrime(n):
            counter+=1
    t1 = time.monotonic_ns()
    print("Found {} in {} milliseconds.".format(counter,abs(t1-t0)/1000000))


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
    print("Platform ......:",sys.implementation)
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

##################################################################################
# main program
##################################################################################
if __name__=='__main__':
    try:
        testPrimeNumber(2000)
        show_hw_info()
    except KeyboardInterrupt:
        pass
    print("end of program")
