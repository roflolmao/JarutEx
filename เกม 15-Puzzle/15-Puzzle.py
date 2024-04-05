#######################################################
### 15-Puzzle
### board: ML4M
### (C) 2021, JarutEx
### https://www.jarutex.com
#######################################################
from machine import Pin,I2C,ADC, DAC
import math
import machine
import gc
import ssd1306
import random
import time
import sys

#######################################################
## System setting
gc.enable()
gc.collect()
machine.freq(240000000)

## ตัวแปรเก็บค่าสุ่มในตาราง 4x4
randPuzzle = [] 
## ตัวแปรเก็บค่า x,y ของลำดับใน randPuzzle เช่น ลำดับที่ 3 ใน randPuzzle คือ posPuzzle[3]
## วึ่งเป็น (3,0) หมายถึง คอลัมน์ 3 แถวแรก ใช้สำหรับตรวจสอบคุณสมบัติของการสลับตำแหน่ง
posPuzzle = (
    (0,0),(1,0),(2,0),(3,0),
    (0,1),(1,1),(2,1),(3,1),
    (0,2),(1,2),(2,2),(3,2),
    (0,3),(1,3),(2,3),(3,3))

#######################################################
## OLED
sclPin = Pin(22)
sdaPin = Pin(21)
spkPin = DAC(Pin(25, Pin.OUT))
i2c = I2C(0,scl=sclPin, sda=sdaPin, freq=400000)
oled = ssd1306.SSD1306_I2C(128,64,i2c)
oled.poweron()
oled.contrast(255)
oled.init_display()
oled.fill(0)
oled.show()

## constant
blockHeight = const(16)
blockWidth = const(16)
screenWidth = const(128)
screenHeight = const(64)
numTiles = const(4)

## Game pad
swA = Pin(32, Pin.IN)
swB = Pin(33, Pin.IN)
swC = Pin(35, Pin.IN)
swD = Pin(34, Pin.IN)
swF = Pin(26, Pin.IN) # select
swE = Pin(27, Pin.IN) # start
jst = (ADC(Pin(39)), ADC(Pin(36))) # X,Y
jst[0].width( ADC.WIDTH_12BIT ) # 12bit
jst[0].atten( ADC.ATTN_11DB ) # 3.3V
jst[1].width( ADC.WIDTH_12BIT ) # 12bit
jst[1].atten( ADC.ATTN_11DB ) # 3.3V

#######################################################
## drawTable()
## แสดงตารางของเกม
#######################################################
def drawTable():
    tileSize = screenHeight//(numTiles+1)
    tableWidth = tileSize*numTiles
    tableHeight = tileSize*numTiles
    left = (screenWidth-tableWidth)//2
    top = (screenHeight-tableHeight)//2
    oled.fill(0)
    for r in range(5):
        oled.hline(left,top+r*tileSize,tableWidth,1)
    for c in range(5):
        oled.vline(left+c*tileSize,top,tableHeight,1)
    i = 0
    for r in range(4):
        for c in range(4):
            if (randPuzzle[i] != "0"):
                oled.text(randPuzzle[i],left+c*tileSize+2,top+r*tileSize+2,1)
            i += 1
    oled.show()

#######################################################
## randomTable()
#######################################################
def beep():
    spkPin.write(255)
    time.sleep_ms(20)
    spkPin.write(0)
    
#######################################################
## randomTable()
## สุ่มค่าในตารางใหม่
#######################################################
def randomTable():
    global randPuzzle
    tmp = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    randPuzzle = []
    for i in range(15):
        data = random.choice(tmp) # สุ่มเลือก
        randPuzzle.append(data) # นำไปเก็บในตาราง
        tmp.remove(data) # ดึงอันที่สุ่มออกไป
    randPuzzle.append(tmp[0]) # ย้ายอันสุดท้ายที่เหลืออยู่มาเก็บในตาราง
    tmp.pop() # นำออก
    tmp=[] # ล้างค่าของตัวแปรลิสต์
    gc.collect()

    
#######################################################
## getInput()
## รับค่าจาก Joystick และ button switch
#######################################################
def getInput():
    left = False
    right = False
    up = False
    down = False
    button1 = False
    button2 = False
    #### Joystick
    jx = 4095-jst[0].read()
    jy = jst[1].read()
    
    if (jx < 1200):
        left = True
    elif (jx > 3000):
        right = True
    if (jy < 1200):
        up = True
    elif (jy > 3000):
        down = True
    # switch
    a = swA.value()
    b = swB.value()
    if (a):
        t0 = time.ticks_ms()
        time.sleep_ms(25)
        a2 = swA.value()
        if (a == a2):
            button1 = True
    if (b):
        t0 = time.ticks_ms()
        time.sleep_ms(25)
        b2 = swB.value()
        if (b == b2):
            button2 = True
    return (left,right,up,down,button1, button2)

#######################################################
## isWin(p)
## ตรวจสอบการชนะเกม
#######################################################
def isWin():
    win = False
    winPuzzle = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','0']
    if (randPuzzle == winPuzzle):
        win = True
    return win    

#######################################################
## find0()
#######################################################
def find0():
    pos = randPuzzle.index("0")
    return (posPuzzle[pos][0],posPuzzle[pos][1],pos)


#######################################################
## youWin()
#######################################################
def youWin():
    for i in range(32):
        oled.scroll(-1,0)
        oled.show()
    oled.text("You",80,20)
    oled.text("Win",79,30)
    oled.text("Win",80,30)
    oled.text("Win",81,30)
    oled.show()
    for i in range(10):
        oled.invert(False)
        time.sleep_ms(50)
        oled.invert(True)
        time.sleep_ms(50)
    oled.invert(False)
    time.sleep_ms(2000)        

#######################################################
## youLost()
#######################################################
def youLost():
    for i in range(32):
        oled.scroll(1,0)
        oled.show()
    oled.text("You",10,20)
    oled.text("Lost",9,30)
    oled.text("Lost",10,30)
    oled.text("Lost",11,30)
    oled.show()
    for i in range(10):
        oled.invert(False)
        time.sleep_ms(50)
        oled.invert(True)
        time.sleep_ms(50)
    oled.invert(False)
    time.sleep_ms(2000)

#######################################################
## moveControl()
#######################################################
def moveControl():
    global randPuzzle
    while True:
        # หาตำแหน่งของ "0"
        (xp,yp,p) = find0() 
        ## วาด
        drawTable()
        ## ตรวจสอบการชนะ
        if (isWin()):
            youWin()
            break
        ## รับค่า
        (a,d,w,s,n1,n2) = getInput()
        if (n1):
            randomTable()
            (xp,yp,p) = find0()
            youLost()
        if (n2):
            break
        if (a and (not d) and (not w) and (not s)):
            #สลับกับค่าทางขวา 
            if (xp < 3):
                pos = yp*numTiles+(xp+1)
                randPuzzle[p] = randPuzzle[pos]
                randPuzzle[pos] = "0"
                beep()
        if ((not a) and (d) and (not w) and (not s)):
            # สลับกับค่าทางซ้าย 
            if (xp > 0):
                pos = yp*numTiles+(xp-1)
                randPuzzle[p] = randPuzzle[pos]
                randPuzzle[pos] = "0"
                beep()
        if ((not a) and (not d) and (w) and (not s)):
            # สลับกับค่าด้านล่าง 
            if (yp < 3):
                pos = (yp+1)*numTiles+xp
                randPuzzle[p] = randPuzzle[pos]
                randPuzzle[pos] = "0" 
                beep()
        if ((not a) and (not d) and (not w) and (s)):
            # สลับกับค่าด้านบน
            if (yp >0):
                pos = (yp-1)*numTiles+xp
                randPuzzle[p] = randPuzzle[pos]
                randPuzzle[pos] = "0" 
                beep()
        time.sleep_ms(100)


#######################################################
### Main program
#######################################################
beep()
randomTable()
moveControl()
oled.poweroff()
beep()
