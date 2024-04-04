# code18-9
from st7735 import TFT
from machine import SPI,Pin
import machine as mc
import time
import math
import ulab as np

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

spi = SPI(1, baudrate=20000000,
          sck=Pin(14), mosi=Pin(13),
          polarity=0, phase=0)
# dc, rst, cs
tft=TFT(spi,2,None,15)
tft.init_7735(tft.GREENTAB80x160)


def rotate(pX,pY,angle):
    rad = math.radians(angle)
    xCos = pX*np.vector.cos(rad)
    ySin = pY*np.vector.sin(rad)
    xSin = pX*np.vector.sin(rad)
    yCos = pY*np.vector.cos(rad)
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

# main program
tft.rotation(1)
tft.fill(tft.BLACK)

t0 = time.ticks_us()
pX = np.array([-2,2,2,-2],dtype=np.float)
pY = np.array([2,2,-2,-2],dtype=np.float)
for degree in range(360):
    newP = rotate(pX,pY,degree)
    draw(newP[0],newP[1],tft.WHITE)
    time.sleep_ms(100)
    tft.fill(0)
for degree in range(360):
    newP = rotate(pX,pY,-degree)
    draw(newP[0],newP[1],tft.CYAN)
    time.sleep_ms(100)
    tft.fill(0)
print("ulab: Delta = {} usec".format(time.ticks_us()-t0))

# endof program
time.sleep_ms(2000)
tft.on(False)
spi.deinit()
