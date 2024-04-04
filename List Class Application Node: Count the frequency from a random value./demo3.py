# ต้องการสุ่มค่า 100 ชุด โดยใช้ตัวเลข 0-20 และนับความถี่
import random
from st7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import machine as mc
import time
import math

data = []
freqTable = []
# random 100 items
for i in range(100):
    data.append(random.getrandbits(5)%21)
# processing
data.sort()
freqTableIdx = 0
for i in range(100):
    if (i == 0): # first time
        freqTable.append([data[i],1])
    else:
        if (freqTable[freqTableIdx][0] == data[i]):
            freqTable[freqTableIdx][1] += 1
        else:
            freqTable.append([data[i],1])
            freqTableIdx += 1
            
print("-------------------------")
print("\tData\tFreq.")
print("-------------------------")
sum = 0
for i in range(len(freqTable)):
    print("{}\t{}\t{}".format(i+1, freqTable[i][0],freqTable[i][1]))
    sum += freqTable[i][1]
print("Freq. sum = {}".format(sum))
print("-------------------------")

mc.freq(240000000)
spi = SPI(2, baudrate=27000000,
          sck=Pin(14), mosi=Pin(12),
          polarity=0, phase=0)
# dc, rst, cs
tft=TFT(spi,15,13,2)
tft.init_7735(tft.GREENTAB80x160)

tft.fill(tft.BLACK)
tft.text((10,0),"Freq. Graph",tft.YELLOW, sysfont)
for i in range(len(freqTable)):
    tft.fillrect((20+i*6,78-freqTable[i][1]*3),(3,freqTable[i][1]*3),tft.WHITE)
