#################################################################
# tetris
# JarutEx 2021-11-06
#################################################################
import gc
import os
import sys
import time
import machine as mc
from machine import Pin,SPI
import math
import st7735 as tft
import vga1_16x16 as font
import random
#################################################################
###### setting ##################################################
#################################################################
gc.enable()
gc.collect()

mc.freq(240000000)

spi = SPI(2, baudrate=26000000,
          sck=Pin(14), mosi=Pin(12),
          polarity=0, phase=0)
#### Key
keL = Pin(39, Pin.IN, Pin.PULL_UP)
keU = Pin(34, Pin.IN, Pin.PULL_UP)
keD = Pin(35, Pin.IN, Pin.PULL_UP)
keR = Pin(32, Pin.IN, Pin.PULL_UP)

swM1 = Pin(33, Pin.IN, Pin.PULL_UP)
swM2 = Pin(25, Pin.IN, Pin.PULL_UP)
swA = Pin(26, Pin.IN, Pin.PULL_UP)
swB = Pin(27, Pin.IN, Pin.PULL_UP)

spk = Pin(19,Pin.OUT)
spk.on()
time.sleep(0.1)
spk.off()

# dc, rst, cs
scr = tft.ST7735(spi, 128, 160, dc=Pin(15, Pin.OUT), reset=Pin(13,Pin.OUT), cs=Pin(2, Pin.OUT), rotation=3)
scr.initr()

actors = [
    [ # แบบ1
     [[1,1,1,1], # rotate=0
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]],
     [[1,0,0,0], # rotate=1
      [1,0,0,0],
      [1,0,0,0],
      [1,0,0,0]]
    ],
    [ # แบบ 2
     [[1,1,1,0], # rotate=0
      [1,0,0,0],
      [0,0,0,0],
      [0,0,0,0]],
     [[1,1,0,0], # rotate=1
      [0,1,0,0],
      [0,1,0,0],
      [0,0,0,0]],
     [[0,0,1,0], # rotate=2
      [1,1,1,0],
      [0,0,0,0],
      [0,0,0,0]],
     [[1,1,0,0], # rotate=3
      [1,0,0,0],
      [1,0,0,0],
      [0,0,0,0]]
    ],
    [ # แบบ 3
     [[1,0,0,0], # rotate=0
      [1,1,1,0],
      [0,0,0,0],
      [0,0,0,0]],
     [[1,1,0,0], # rotate=1
      [1,0,0,0],
      [1,0,0,0],
      [0,0,0,0]],
     [[1,1,1,0], # rotate=2
      [0,0,1,0],
      [0,0,0,0],
      [0,0,0,0]],
     [[0,1,0,0], # rotate=3
      [0,1,0,0],
      [1,1,0,0],
      [0,0,0,0]]
    ],
    [ # แบบ 4
     [[0,1,0,0], # rotate=0
      [1,1,1,0],
      [0,0,0,0],
      [0,0,0,0]],
     [[1,0,0,0], # rotate=1
      [1,1,0,0],
      [1,0,0,0],
      [0,0,0,0]],
     [[1,1,1,0], # rotate=2
      [0,1,0,0],
      [0,0,0,0],
      [0,0,0,0]],
     [[0,1,0,0], # rotate=3
      [1,1,0,0],
      [0,1,0,0],
      [0,0,0,0]],
    ],
    [ # แบบ 5
     [[0,1,1,0], # rotate=0
      [1,1,0,0],
      [0,0,0,0],
      [0,0,0,0]],
     [[1,0,0,0], # rotate=1
      [1,1,0,0],
      [0,1,0,0],
      [0,0,0,0]]
    ],
    [ # แบบ 6
     [[1,1,0,0], # rotate=0
      [0,1,1,0],
      [0,0,0,0],
      [0,0,0,0]],
     [[0,1,0,0], # rotate=1
      [1,1,0,0],
      [1,0,0,0],
      [0,0,0,0]]
    ],
    [ # แบบ 7
     [[1,1,0,0], # rotate=0
      [1,1,0,0],
      [0,0,0,0],
      [0,0,0,0]]
    ]
]
actorColors = [
    tft.color565(232,232,64),
    tft.color565(232,64,64),
    tft.color565(232,64,232),
    tft.color565(64,64,232),
    tft.color565(64,232,64),
    tft.color565(64,232,232),
    tft.color565(232,232,232)
]
actorRotate = 0
actorNo = random.randint(0,len(actors)-1)
maxCol = 10
maxRow = 16
posX = 0
posY = 0

#################################################################
###### sub modules ##############################################
#################################################################
def splash():
    scr.fill(tft.color565(0x00,0x00,0x00))
    scr.text(font,"JarutEx", 20, 20, tft.YELLOW, tft.BLACK)
    scr.text(font,"JarutEx", 21, 20, tft.YELLOW, tft.BLACK)
    scr.text(font,"(C)2021", 40,48, tft.CYAN, tft.BLACK)
    time.sleep_ms(2000)
    scr.fill(tft.BLACK)

def table():
    blankColor = tft.color565(48, 48, 48)
    for i in range(maxRow):
        for j in range(maxCol):
            x = j * 8 + 1
            y = i * 8 + 1
            w = 6
            h = 6
            scr.fill_rect(x,y,w,h, blankColor)

def draw():
    actor = actors[actorNo][actorRotate]
    for i in range(4):
        for j in range(4):
            if actor[i][j]:
                x = (posX+j) * 8 + 1
                y = (posY+i) * 8 + 1
                w = 6
                h = 6
                scr.fill_rect(x,y,w,h,actorColors[actorNo])


#################################################################
###### main program #############################################
#################################################################
splash()
table()
draw()
while swM1.value():
    if swM2.value() == 0:
        table()
        actorNo = random.randint(0,len(actors)-1)
        posX = 0
        posY = 0
        actorRotate = 0
        draw()
    if swA.value() == 0: # rotate
        table()
        if (actorNo == 0):
            actorRotate += 1
            if actorRotate > 1:
                if (posX > (maxCol-4)): # ถ้้าตำแหน่งเกินขอบให้หมุนกลับไปตำแหน่งที่เหมาะสม
                    actorRotate = 1
                else:
                    actorRotate = 0
        elif (actorNo == 1):
            if actorRotate == 0:
                actorRotate = 1
            elif actorRotate == 1:
                if (posX < (maxCol - 2)):
                    actorRotate = 2
                else:
                    actorRotate = 1
            elif actorRotate == 2:
                actorRotate = 3
            else:
                if (posX < (maxCol - 2)):
                    actorRotate = 0
                else:
                    actorRotate = 3
        elif (actorNo == 2):
            if actorRotate == 0:
                actorRotate = 1
            elif actorRotate == 1:
                if (posX < (maxCol - 2)):
                    actorRotate = 2
                else:
                    actorRotate = 1
            elif actorRotate == 2:
                actorRotate = 3
            else:
                if (posX < (maxCol - 2)):
                    actorRotate = 0
                else:
                    actorRotate = 3
        elif (actorNo == 3):
            if actorRotate == 0:
                actorRotate = 1
            elif actorRotate == 1:
                if (posX < (maxCol - 2)):
                    actorRotate = 2
                else:
                    actorRotate = 1
            elif actorRotate == 2:
                actorRotate = 3
            else:
                if (posX < (maxCol - 2)):
                    actorRotate = 0
                else:
                    actorRotate = 3
        elif (actorNo == 4):
            if actorRotate == 0:
                actorRotate = 1
            else:
                if (posX < (maxCol - 2)):
                    actorRotate = 0
                else:
                    actorRotate = 1
        elif (actorNo == 5):
            if actorRotate == 0:
                actorRotate = 1
            else:
                if (posX < (maxCol - 2)):
                    actorRotate = 0
                else:
                    actorRotate = 1
        draw()
    if keL.value() == 0:
        if posX > 0:
            table()
            posX -= 1
            draw()
    if keR.value() == 0:
        if (actorNo == 0):
            if (actorRotate == 0):
                maxX = maxCol-4
            else:
                maxX = maxCol-1
            if posX < maxX:
                table()
                posX += 1
                draw()
        elif (actorNo == 1):
            if (actorRotate == 0):
                maxX = maxCol-3
            elif (actorRotate == 1):
                maxX = maxCol-2
            elif (actorRotate == 2):
                maxX = maxCol-3
            else:
                maxX = maxCol-2
            if posX < maxX:
                table()
                posX += 1
                draw()
        elif (actorNo == 2):
            if (actorRotate == 0):
                maxX = maxCol-3
            elif (actorRotate == 1):
                maxX = maxCol-2
            elif (actorRotate == 2):
                maxX = maxCol-3
            else:
                maxX = maxCol-2
            if posX < maxX:
                table()
                posX += 1
                draw()
        elif (actorNo == 3):
            if (actorRotate == 0):
                maxX = maxCol-3
            elif (actorRotate == 1):
                maxX = maxCol-2
            elif (actorRotate == 2):
                maxX = maxCol-3
            else:
                maxX = maxCol-2
            if posX < maxX:
                table()
                posX += 1
                draw()
        elif (actorNo == 4):
            if (actorRotate == 0):
                maxX = maxCol-3
            else:
                maxX = maxCol-2
            if posX < maxX:
                table()
                posX += 1
                draw()
        elif (actorNo == 5):
            if (actorRotate == 0):
                maxX = maxCol-3
            else:
                maxX = maxCol-2
            if posX < maxX:
                table()
                posX += 1
                draw()
        elif (actorNo == 6):
            if posX < (maxCol-2):
                table()
                posX += 1
                draw()
    time.sleep_ms(100)
scr.fill(0)
spi.deinit()
