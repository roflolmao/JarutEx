#################################################################
# tetris Ep3
# JarutEx 2021-11-08
#################################################################
import gc
import os
import sys
import time
import machine as mc
from machine import Pin,SPI, Timer
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

scr = tft.ST7735(spi, 128, 160, dc=Pin(15, Pin.OUT), reset=Pin(13,Pin.OUT), cs=Pin(2, Pin.OUT), rotation=3)
scr.initr()

Tmr = Timer(0)

field = []
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
     [[1,0,0,0], # rotate=3
      [1,0,0,0],
      [1,1,0,0],
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
blankColor = tft.color565(48, 48, 48)
filledColor = tft.color565(192,192,192)
updated = False
gameOver = False

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

def genTable():
    global field
    for i in range(maxRow):
        row = []
        for j in range(maxCol):
            row.append(0)
        field.append(row)

def table(rowStart=0, rowEnd=maxRow):
    for i in range(rowStart, rowEnd,1):
        for j in range(maxCol):
            x = j * 8 + 1
            y = i * 8 + 1
            w = 6
            h = 6
            if (field[i][j] == 0):
                scr.fill_rect(x,y,w,h, blankColor)
            else:
                scr.fill_rect(x,y,w,h, filledColor)

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
                
def cbFalling(x):
    global posY,posX,actorRotate, actorNo, updated, gameOver, Tmr, Render
    posY += 1
    lastRow = 14
    if actorNo == 0:
        if actorRotate == 0:
            lastRow = 15
        else:
            lastRow = 12
    elif actorNo == 1:
        if actorRotate == 0:
            lastRow = 14
        elif actorRotate == 1:
            lastRow = 13
        elif actorRotate == 2:
            lastRow = 14
        else:
            lastRow = 13
    elif actorNo == 2:
        if actorRotate == 0:
            lastRow = 14
        elif actorRotate == 1:
            lastRow = 13
        elif actorRotate == 2:
            lastRow = 14
        else:
            lastRow = 13
    elif actorNo == 3:
        if actorRotate == 0:
            lastRow = 14
        elif actorRotate == 1:
            lastRow = 13
        elif actorRotate == 2:
            lastRow = 14
        else:
            lastRow = 13
    elif actorNo == 4:
        if actorRotate == 0:
            lastRow = 14
        else:
            lastRow = 13
    elif actorNo == 5:
        if actorRotate == 0:
            lastRow = 14
        else:
            lastRow = 13
    else:
        lastRow = 14
    
    if (posY > lastRow):
        for i in range(4):
            for j in range(4):
                if actors[actorNo][actorRotate][i][j] == 1:
                    field[posY+i-1][posX+j] = 1
        removeRow()
        table()
        newItem()
    else:
        if (isCollide()):
            for i in range(4):
                for j in range(4):
                    if actors[actorNo][actorRotate][i][j] == 1:
                        field[posY+i-1][posX+j] = 1
            removeRow()
            table()
            newItem()
            if (isCollide()): 
                gameOver = True
                Tmr.deinit()
                Render.deinit()
                return
    updated = True

def newItem():
    global actorNo, posX, posY, actorRotate
    actorNo = random.randint(0,len(actors)-1)
    posX = 0
    posY = 0
    actorRotate = 0

def isCollide():
    if actorNo == 0:
        if actorRotate == 0:
            for j in range(4):
                if (actors[actorNo][actorRotate][0][j] & field[posY][posX+j]):
                    return True
        else:
            for i in range(4):
                if (actors[actorNo][actorRotate][i][0] & field[posY+i][posX]):
                    return True
    else:
        if actorNo in [1,2,3]:
            if actorRotate in [0,2]:
                for i in range(2):
                    for j in range(3):
                        if (actors[actorNo][actorRotate][i][j] & field[posY+i][posX+j]):
                            return True
            else:
                for i in range(3):
                    for j in range(2):
                        if (actors[actorNo][actorRotate][i][j] & field[posY+i][posX+j]):
                            return True
        elif actorNo in [4,5]:
            if actorRotate == 0:
                for i in range(2):
                    for j in range(3):
                        if (actors[actorNo][actorRotate][i][j] & field[posY+i][posX+j]):
                            return True
            else:
                for i in range(3):
                    for j in range(2):
                        if (actors[actorNo][actorRotate][i][j] & field[posY+i][posX+j]):
                            return True
        else:
            for i in range(2):
                for j in range(2):
                    if (actors[actorNo][actorRotate][i][j] & field[posY+i][posX+j]):
                        return True
    return False

def cbRender(x):
    global posY,posX,actorRotate, actorNo, updated
    if swA.value() == 0: # rotate
        if (actorNo == 0):
            if (actorRotate == 0):
                if (posX > (maxCol-4))
                    pass
                else:
                    actorRotate = 1
                    if (isCollide()):
                        actorRotate = 0
                    else:
                        updated = True
            else:
                if (posY > maxRow-4):
                    pass
                else: 
                    actorRotate = 0
                    if (isCollide()):
                        actorRotate = 1
                    else:
                        updated = True
        elif (actorNo == 1):
            if actorRotate == 0:
                actorRotate = 1
                if (isCollide()):
                    actorRotate = 0
                else:
                    updated = True
            elif actorRotate == 1:
                if (posX < (maxCol - 2)):
                    actorRotate = 2
                    if (isCollide()):
                        actorRotate = 1
                    else:
                        updated = True
                else:
                    actorRotate = 1
            elif actorRotate == 2:
                actorRotate = 3
                updated = True
            else:
                if (posX < (maxCol - 2)):
                    actorRotate = 0
                    updated = True
                else:
                    actorRotate = 3
        elif (actorNo == 2):
            if actorRotate == 0:
                actorRotate = 1
                updated = True
            elif actorRotate == 1:
                if (posX < (maxCol - 2)):
                    actorRotate = 2
                    updated = True
                else:
                    actorRotate = 1
            elif actorRotate == 2:
                actorRotate = 3
                updated = True
            else:
                if (posX < (maxCol - 2)):
                    actorRotate = 0
                    updated = True
                else:
                    actorRotate = 3
        elif (actorNo == 3):
            if actorRotate == 0:
                actorRotate = 1
                updated = True
            elif actorRotate == 1:
                if (posX < (maxCol - 2)):
                    actorRotate = 2
                    updated = True
                else:
                    actorRotate = 1
            elif actorRotate == 2:
                actorRotate = 3
                updated = True
            else:
                if (posX < (maxCol - 2)):
                    actorRotate = 0
                    updated = True
                else:
                    actorRotate = 3
        elif (actorNo == 4):
            if actorRotate == 0:
                actorRotate = 1
                updated = True
            else:
                if (posX < (maxCol - 2)):
                    actorRotate = 0
                    updated = True
                else:
                    actorRotate = 1
        elif (actorNo == 5):
            if actorRotate == 0:
                actorRotate = 1
                updated = True
            else:
                if (posX < (maxCol - 2)):
                    actorRotate = 0
                    updated = True
                else:
                    actorRotate = 1
    if keL.value() == 0:
        if posX > 0:
            posX -= 1
            if isCollide():
                posX += 1
            else:
                updated = True
    if keR.value() == 0:
        if (actorNo == 0):
            if (actorRotate == 0):
                maxX = maxCol-4
            else:
                maxX = maxCol-1
            if posX < maxX:
                posX += 1
                if (isCollide()):
                    posX -= 1
                else:
                    updated = True
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
                posX += 1
                if (isCollide()):
                    posX -= 1
                else:
                    updated = True
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
                posX += 1
                if (isCollide()):
                    posX -= 1
                else:
                    updated = True
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
                posX += 1
                if (isCollide()):
                    posX -= 1
                else:
                    updated = True
        elif (actorNo == 4):
            if (actorRotate == 0):
                maxX = maxCol-3
            else:
                maxX = maxCol-2
            if posX < maxX:
                posX += 1
                if (isCollide()):
                    posX -= 1
                else:
                    updated = True
        elif (actorNo == 5):
            if (actorRotate == 0):
                maxX = maxCol-3
            else:
                maxX = maxCol-2
            if posX < maxX:
                posX += 1
                if (isCollide()):
                    posX -= 1
                else:
                    updated = True
        elif (actorNo == 6):
            if posX < (maxCol-2):
                posX += 1
                if (isCollide()):
                    posX -= 1
                else:
                    updated = True
    if (updated):
        startY = 0
        endY = posY
        if posY > 0:
            startY = posY-1
        if endY >= maxRow:
            endY = maxRow
        if actorNo == 0:
            endY += 4
        elif actorNo == 1:
            endY += 3
        elif actorNo == 2:
            endY += 3
        elif actorNo == 3:
            endY += 3
        elif actorNo == 4:
            endY += 3
        elif actorNo == 5:
            endY += 3
        else:
            endY += 2
        if endY >= maxRow:
            endY = maxRow
        table(startY,endY)
        draw()
        updated = False
        
def removeRow():
    row = maxRow-1
    while row > 0:
        if ([1,1,1,1,1,1,1,1,1,1] == field[row]):
            if (row == 0): 
                field[row] = [0,0,0,0,0,0,0,0,0,0]
            else: 
                for r in range(row, 1, -1):
                    field[r] = field[r-1]
                field[0] = [0,0,0,0,0,0,0,0,0,0]
        else:
            row = row - 1


#################################################################
###### main program #############################################
#################################################################
splash()
genTable()
table()
draw()
Render = Timer(1)
Tmr.init( period=1000, mode=Timer.PERIODIC, callback=cbFalling)
Render.init( period=100, mode=Timer.PERIODIC, callback=cbRender)
while swM1.value():
    if gameOver:
        scr.text(font," Game ", 40, 40, tft.YELLOW, tft.RED)
        scr.text(font," Over ", 40, 56, tft.YELLOW, tft.RED)
        break
scr.fill(0)
spi.deinit()
