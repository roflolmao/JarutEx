import os
import gc
import sys
import time as tm
import machine as mc

gc.enable()
gc.collect()

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
    t0 = tm.ticks_ms() #tm.monotonic()
    for n in range(2, maxN):
        if isPrime(n):
            counter+=1
    t1 = tm.ticks_ms() #tm.monotonic()
    print("testPrineNumner({}) ... Found {} in {} msecs.".format(maxN,counter,abs(t1-t0)))


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
    print("Platform ......:",sys.implementation[0])
    print("Version .......:",sys.version)
    print("Frequency")
    print("   CPU ........: {}Hz".format(mc.freq()[0]))
    print("   AHB ........: {}Hz".format(mc.freq()[1]))
    print("   APB1 .......: {}Hz".format(mc.freq()[2]))
    print("   APB2 .......: {}Hz".format(mc.freq()[3]))
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

if __name__=='__main__':
    show_hw_info()
    testPrimeNumber(2000)
