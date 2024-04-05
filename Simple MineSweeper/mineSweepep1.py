#################################################################
# mineSweep Part 1
# JarutEx 2021-11-12
# 128x160
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

# dc, rst, cs
scr = tft.ST7735(spi, 128, 160, dc=Pin(15, Pin.OUT), reset=Pin(13,Pin.OUT), cs=Pin(2, Pin.OUT), rotation=3)
scr.initr()

Tmr = Timer(0)
Render = Timer(1)
bgColor = tft.color565(0x96,0x24,0x24)
updated = False
gameOver = False
maxRow = const(6)
maxCol = const(8)
table = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]
posX = 0
posY = 0

#################################################################
###### sub modules ##############################################
#################################################################
def splash():
    scr.fill(bgColor)
    scr.text(font,"mine", 20, 42, tft.YELLOW, bgColor)
    for i in range(200):
        color = tft.color565(55+i,55+i,55+i)
        scr.text(font,"Sweep", 56, 60, color, bgColor)
        time.sleep_ms(10)
    time.sleep_ms(2000)

def randomTable():
    global table
    table = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ] 
    counter = 0
    while (counter < 10):
        x = random.randint(1,maxCol)-1
        y = random.randint(1,maxRow)-1
        if (table[y][x] == 0):
            # print("Bomb no.{} at ({},{}).".format(counter+1,x,y))
            table[y][x] = 9
            counter+=1
    ## เติมตัวเลข
    for row in range(maxRow):
        for col in range(maxCol):
            sum = 0
            if (table[row][col] != 9):
                if (row == 0): # แถวแรก
                    if col == 0: # คอลัมน์แรก
                        if (table[row][col+1]==9): # ขวา
                            sum += 1
                        if (table[row+1][col]==9): # ด้านล่าง
                            sum += 1
                        if (table[row+1][col+1]==9): # มุมขวาล่าง
                            sum += 1
                    elif col == maxCol-1: # คอลัมน์สุดท้าย
                        if (table[row][col-1]==9): # ซ้าย
                            sum += 1
                        if (table[row+1][col-1]==9): # มุมซ้ายล่าง
                            sum += 1
                        if (table[row+1][col]==9): # ด้านล่าง
                            sum += 1
                    else: # คอลัมน์อื่น ๆ
                        if (table[row][col-1]==9): # ซ้าย
                            sum += 1
                        if (table[row][col+1]==9): # ขวา
                            sum += 1
                        if (table[row+1][col-1]==9): # มุมซ้ายล่าง
                            sum += 1
                        if (table[row+1][col]==9): # ด้านล่าง
                            sum += 1
                        if (table[row+1][col+1]==9): # มุมขวาล่าง
                            sum += 1
                elif (row == maxRow-1): # แถวสุดท้าย
                    if col == 0: # คอลัมน์แรก
                        if (table[row-1][col]==9): # ด้านบน
                            sum += 1
                        if (table[row-1][col+1]==9): # มุมขวาบน
                            sum += 1
                        if (table[row][col+1]==9): # ขวา
                            sum += 1
                    elif col == maxCol-1: # คอลัมน์สุดท้าย
                        if (table[row-1][col-1]==9): # มุมซ้ายบน
                            sum += 1
                        if (table[row-1][col]==9): # ด้านบน
                            sum += 1
                        if (table[row][col-1]==9): # ซ้าย
                            sum += 1
                    else: # คอลัมน์อื่น ๆ
                        if (table[row-1][col-1]==9): # มุมซ้ายบน
                            sum += 1
                        if (table[row-1][col]==9): # ด้านบน
                            sum += 1
                        if (table[row-1][col+1]==9): # มุมขวาบน
                            sum += 1
                        if (table[row][col-1]==9): # ซ้าย
                            sum += 1
                        if (table[row][col+1]==9): # ขวา
                            sum += 1
                else:
                    if col == 0: # คอลัมน์แรก
                        if (table[row-1][col]==9): # ด้านบน
                            sum += 1
                        if (table[row-1][col+1]==9): # มุมขวาบน
                            sum += 1
                        if (table[row][col+1]==9): # ขวา
                            sum += 1
                        if (table[row+1][col]==9): # ด้านล่าง
                            sum += 1
                        if (table[row+1][col+1]==9): # มุมขวาล่าง
                            sum += 1
                    elif col == maxCol-1: # คอลัมน์สุดท้าย
                        if (table[row-1][col-1]==9): # มุมซ้ายบน
                            sum += 1
                        if (table[row-1][col]==9): # ด้านบน
                            sum += 1
                        if (table[row][col-1]==9): # ซ้าย
                            sum += 1
                        if (table[row+1][col-1]==9): # มุมซ้ายล่าง
                            sum += 1
                        if (table[row+1][col]==9): # ด้านล่าง
                            sum += 1
                    else: # คอลัมน์อื่น ๆ
                        if (table[row-1][col-1]==9): # มุมซ้ายบน
                            sum += 1
                        if (table[row-1][col]==9): # ด้านบน
                            sum += 1
                        if (table[row-1][col+1]==9): # มุมขวาบน
                            sum += 1
                        if (table[row][col-1]==9): # ซ้าย
                            sum += 1
                        if (table[row][col+1]==9): # ขวา
                            sum += 1
                        if (table[row+1][col-1]==9): # มุมซ้ายล่าง
                            sum += 1
                        if (table[row+1][col]==9): # ด้านล่าง
                            sum += 1
                        if (table[row+1][col+1]==9): # มุมขวาล่าง
                            sum += 1
                table[row][col] = sum

def cbInput(x):
    global updated, posX, posY
    ####################################################### 
    ##### Input
    ####################################################### 
    if (swM2.value() == 0):
        randomTable()
        updated = True
        
    ####################################################### 
    ##### Input : เลื่อนไปทางซ้าย
    ####################################################### 
    if keL.value() == 0:
        #updated = True
        if (posX > 0):
            cursor(False)
            posX -= 1
            cursor()

    ####################################################### 
    ##### Input : เลื่อนไปทางขวา
    ####################################################### 
    if keR.value() == 0:
        #updated = True
        if (posX < maxCol-1):
            cursor(False)
            posX += 1
            cursor()
            
    ####################################################### 
    ##### Input : เลื่อนไปด้านบน
    ####################################################### 
    if keU.value() == 0:
        #updated = True
        if (posY > 0):
            cursor(False)
            posY -= 1
            cursor()

    ####################################################### 
    ##### Input : เลื่อนไปด้านล่าง
    ####################################################### 
    if keD.value() == 0:
        #updated = True
        if (posY < maxRow-1):
            cursor(False)
            posY += 1
            cursor()

def cbRender(x):
    global updated
    ####################################################### 
    ##### อัพเดตหน้าจอ
    ####################################################### 
    if (updated):
        draw()
        updated = False
        

def draw():
    w = 20
    h = 20
    for row in range(6):
        y = row*h+4+2
        for col in range(8):
            x = col*w+2
            if table[row][col]:
                if (table[row][col]== 9):
                    scr.fill_rect(x,y,w-4,h-4, bgColor)
                    scr.text(font,"*",x,y,tft.YELLOW,bgColor)
                else:
                    scr.fill_rect(x,y,w-4,h-4, tft.BLUE)
                    scr.text(font,"{}".format(table[row][col]),x,y,tft.WHITE,tft.BLUE)                
            else:
                scr.fill_rect(x,y,w-4,h-4, tft.BLUE)

def cursor(marked=True):
    w = 20
    h = 20
    if marked:
        scr.rect(posX*w,posY*h+4,w,h,tft.WHITE)
    else:
        scr.rect(posX*w,posY*h+4,w,h,tft.BLACK)


#################################################################
###### main program #############################################
#################################################################
#splash()
randomTable()
scr.fill(tft.BLACK)
draw()
cursor()
Tmr.init( period=200, mode=Timer.PERIODIC, callback=cbInput)
Render.init( period=100, mode=Timer.PERIODIC, callback=cbRender)
while swM1.value():
    pass
scr.fill(0)
Tmr.deinit()
Render.deinit()
spi.deinit()
