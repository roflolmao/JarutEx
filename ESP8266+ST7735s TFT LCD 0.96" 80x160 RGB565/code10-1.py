#code10-1
from st7735 import TFT
from machine import SPI,Pin
import machine as mc
import time
import math
mc.freq(160000000)
spi = SPI(1, baudrate=20000000,polarity=0, phase=0)
# dc, rst, cs
tft=TFT(spi,16)
tft.init_7735(tft.GREENTAB80x160)

def testlines(color):
    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((0,0),(x, tft.size()[1] - 1), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((0,0),(tft.size()[0] - 1, y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((tft.size()[0] - 1, 0), (x, tft.size()[1] - 1), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((tft.size()[0] - 1, 0), (0, y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((0, tft.size()[1] - 1), (x, 0), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((0, tft.size()[1] - 1), (tft.size()[0] - 1,y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((tft.size()[0] - 1, tft.size()[1] - 1), (x, 0), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((tft.size()[0] - 1, tft.size()[1] - 1), (0, y), color)

def testfastlines(color1, color2):
    tft.fill(TFT.BLACK)
    for y in range(0, tft.size()[1], 5):
        tft.hline((0,y), tft.size()[0], color1)
    for x in range(0, tft.size()[0], 5):
        tft.vline((x,0), tft.size()[1], color2)

def testdrawrects(color):
    tft.fill(TFT.BLACK);
    for x in range(0,tft.size()[0],6):
        tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color)

def testfillrects(color1, color2):
    tft.fill(TFT.BLACK);
    for x in range(tft.size()[0],0,-6):
        tft.fillrect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color1)
        tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color2)

def testfillcircles(radius, color):
    for x in range(radius, tft.size()[0], radius * 2):
        for y in range(radius, tft.size()[1], radius * 2):
            tft.fillcircle((x, y), radius, color)

def testdrawcircles(radius, color):
    for x in range(0, tft.size()[0] + radius, radius * 2):
        for y in range(0, tft.size()[1] + radius, radius * 2):
            tft.circle((x, y), radius, color)

def testtriangles():
    tft.fill(TFT.BLACK);
    color = 0xF800
    w = tft.size()[0] // 2
    x = tft.size()[1] - 1
    y = 0
    z = tft.size()[0]
    for t in range(0, 15):
        tft.line((w, y), (y, x), color)
        tft.line((y, x), (z, x), color)
        tft.line((z, x), (w, y), color)
        x -= 4
        y += 4
        z -= 4
        color += 100

def testroundrects():
    tft.fill(TFT.BLACK);
    color = 100
    for t in range(5):
        x = 0
        y = 0
        w = tft.size()[0] - 2
        h = tft.size()[1] - 2
        for i in range(17):
            tft.rect((x, y), (w, h), color)
            x += 2
            y += 3
            w -= 4
            h -= 6
            color += 1100
        color += 100

tft.fill(TFT.BLACK)
testlines(TFT.YELLOW)
time.sleep_ms(500)

testfastlines(TFT.RED, TFT.BLUE)
time.sleep_ms(500)

testdrawrects(TFT.GREEN)
time.sleep_ms(500)

testfillrects(TFT.YELLOW, TFT.PURPLE)
time.sleep_ms(500)

tft.fill(TFT.BLACK)
testfillcircles(10, TFT.BLUE)
testdrawcircles(10, TFT.WHITE)
time.sleep_ms(500)

testroundrects()
time.sleep_ms(500)

testtriangles()
time.sleep_ms(2000)
tft.on(False)
