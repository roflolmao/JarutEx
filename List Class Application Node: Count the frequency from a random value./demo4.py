import random
from st7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import machine as mc
import time
import math

maxData = const(10000)
data = []
freqTable = []
graphHeight = const(30)
minY = maxData
maxY = 1

mc.freq(240000000)
spi = SPI(2, baudrate=30000000,
          sck=Pin(14), mosi=Pin(12),
          polarity=0, phase=0)
# dc, rst, cs
tft=TFT(spi,15,13,2)
tft.init_7735(tft.GREENTAB80x160)

tft.fill(tft.BLACK)
tft.text((10,36),"(C)2020-21",tft.YELLOW,sysfont)
tft.text((92,36),"JarutEx",tft.WHITE,sysfont)
tft.text((93,36),"JarutEx",tft.WHITE,sysfont)


time.sleep_ms(1000)
tft.fill(tft.BLACK)
tft.text((10,0), "Freq. Graph",tft.YELLOW,sysfont)

# random 100 items
for i in range(maxData):
    data.append(random.getrandbits(5)%21)
# processing
data.sort()
freqTableIdx = 0
for i in range(maxData):
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
    if minY > freqTable[i][1]:
        minY = freqTable[i][1]
    if maxY < freqTable[i][1]:
        maxY = freqTable[i][1]
    sum += freqTable[i][1]

print("Freq. sum = {}".format(sum))
print("-------------------------")

tft.text((10,10),"min={} max={}".format(minY,maxY),tft.WHITE,sysfont)
scale = math.fabs(maxY-minY) # หาความยาวของช่วงค่า
#print("Scale = {} [{}-{}]".format(scale,minY,maxY))
for i in range(len(freqTable)):
    data = int(graphHeight*(freqTable[i][1]/scale))
    gColor = tft.color(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8))
    tft.fillrect((20+i*6,78-data),(3,data),gColor)
