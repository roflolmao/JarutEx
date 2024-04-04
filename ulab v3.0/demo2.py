import gc
import os
import sys
import ulab
import time
import math
import machine as mc
from ulab import numpy as np
from st7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin

gc.enable()
gc.collect()
mc.freq(240000000)

minX = -10.0
maxX = 10.0
minY = -5.0
maxY = 5.0
scrWidth = const(160)
scrHeight = const(80)
ratioX = float(scrWidth)/(math.fabs(minX)+math.fabs(maxX)+1)
ratioY = float(scrHeight)/(math.fabs(minY)+math.fabs(maxY)+1)
centerX = const(scrWidth >> 1)
centerY = const(scrHeight >> 1)

spi = SPI(2, baudrate=27000000,
          sck=Pin(14), mosi=Pin(12),
          polarity=0, phase=0)
# dc, rst, cs
tft=TFT(spi,15,13,2)
tft.init_7735(tft.GREENTAB80x160)
tft.fill(TFT.BLACK)

def rotate(pX,pY,angle):
    rad = math.radians(angle)
    xCos = pX*np.cos(rad)
    ySin = pY*np.sin(rad)
    xSin = pX*np.sin(rad)
    yCos = pY*np.cos(rad)
    newX = xCos - ySin
    newY = xSin + yCos
    return (newX, newY)

def draw(pX, pY,aColor=tft.WHITE):
    newPx = np.array(pX*ratioX+centerX,dtype=np.uint16)
    newPy = np.array(pY*ratioY+centerY,dtype=np.uint16)
    tft.line((newPx[0],newPy[0]),(newPx[1],newPy[1]),aColor)
    tft.line((newPx[1],newPy[1]),(newPx[2],newPy[2]),aColor)
    tft.line((newPx[2],newPy[2]),(newPx[3],newPy[3]),aColor)
    tft.line((newPx[3],newPy[3]),(newPx[0],newPy[0]),aColor)

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
    print("   usage ......:", rom_usage,"KB",rusage_percent )
    print("   Free .......:", rom_free,"KB",rfree_percent )
    print("system name ...:",uname.sysname)
    print("node name .....:",uname.nodename)
    print("release .......:",uname.release)
    print("version .......:",uname.version)
    print("machine .......:",uname.machine)

def show_ulab():
    print("ulab version {}.".format(ulab.__version__))
    
# main program
if __name__=="__main__":
    show_hw_info()
    show_ulab()
    tft.rotation(1)
    tft.fill(tft.BLACK)
    t0 = time.ticks_us()
    pX = np.array([-2,2,2,-2],dtype=np.float)
    pY = np.array([2,2,-2,-2],dtype=np.float)
    for degree in range(360):
        newP = rotate(pX,pY,degree)
        draw(newP[0],newP[1],tft.WHITE)
        #time.sleep_ms(100)
        tft.fill(0)
    for degree in range(360):
        newP = rotate(pX,pY,-degree)
        draw(newP[0],newP[1],tft.CYAN)
        #time.sleep_ms(100)
        tft.fill(0)
    print("ulab: Delta = {} usec".format(time.ticks_us()-t0))

    # endof program
    time.sleep_ms(2000)
    tft.on(False)
    spi.deinit()
