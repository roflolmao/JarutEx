#######################################################
### Tic-Tac-Toe
### board: ML4M
### (C) 2021, JarutEx
### www.jarutex.com
#######################################################
from machine import Pin,I2C,ADC
import math
import machine
import gc
import ssd1306
import random
import time

#######################################################
## System setting
gc.enable()
gc.collect()
machine.freq(240000000)

#######################################################
## OLED
sclPin = Pin(22)
sdaPin = Pin(21)
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


## Gobal variables
table = ["","","","","","","","",""]
userPos = 0


#######################################################
## drawTable()
## แสดงตารางของเกม
#######################################################
def drawTable():
    oled.fill(0)
    left = (screenWidth - (blockWidth*3))//2
    top = (screenHeight - (blockHeight*3))//2
    for i in range(4):
        oled.hline(left-(blockWidth//4),(top-(blockHeight//4))+blockHeight*i, blockWidth*3,1)
        oled.vline((left-(blockWidth//4))+(i*blockWidth),top-(blockHeight//4), blockWidth*3,1)
    i = 0
    for r in range(3):
        for c in range(3):
            oled.text(str(table[i]),left+blockWidth*c,top+blockHeight*r)
            i += 1
    oled.show()
    
#######################################################
## getInput()
## รับค่าจาก Joystick และ button switch
#######################################################
def getInput():
    left = False
    right = False
    up = False
    down = False
    button = False
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
    b = swB.value()
    if (b):
        t0 = time.ticks_ms()
        time.sleep_ms(100)
        b2 = swB.value()
        if (b == b2):
            button = True
    return (left,right,up,down,button)

#######################################################
## isWin(p)
## ตรวจว่า p ครบตามเงื่อนไขการชนะหรือไม่
#######################################################
def isWin(p):
    win = False
    # case 1 : แถวแรกเป็น p
    if ((table[0]==p)and(table[1]==p)and(table[2]==p)):
        win = True
    # case 2 : แถวที่ 2 เป็น p
    if ((table[3]==p)and(table[4]==p)and(table[5]==p)):
        win = True
    # case 3 : แถวที่ 3 เป็น p
    if ((table[6]==p)and(table[7]==p)and(table[8]==p)):
        win = True
    # case 4 : คอลัมน์ 0 เป็น p
    if ((table[0]==p)and(table[3]==p)and(table[6]==p)):
        win = True
    # case 5 : คอลัมน์ 1 เป็น p
    if ((table[1]==p)and(table[4]==p)and(table[7]==p)):
        win = True
    # case 6 : คอลัมน์ 2 เป็น p
    if ((table[2]==p)and(table[5]==p)and(table[8]==p)):
        win = True
    # case 7 : แนวทแยงมุมซ้ายบนลงงล่างขวา
    if ((table[0]==p)and(table[4]==p)and(table[8]==p)):
        win = True
    # case 8 : แนวทแยงมุมจากซ้ายล่างขึ้นบนขวา
    if ((table[2]==p)and(table[4]==p)and(table[6]==p)):
        win = True
    return win    


#######################################################
## testControl2()
## ทดสอบขยับกล่องสี่เหลี่ยมด้วยคันโยกและออกด้วย swB
#######################################################
posX=0
posY=0
xResponse = const(2)
yResponse = const(2)
def testControl2():
    global table, posX, posY
    x = (posX<<xResponse)
    y = (posY<<yResponse)
    while True:
        ## ล้างหน้าจอ
        oled.fill(0)
        ## วาดตาราง
        left = (screenWidth - (blockWidth*3))//2
        top = (screenHeight - (blockHeight*3))//2
        for i in range(4):
            oled.hline(left-(blockWidth//4),(top-(blockHeight//4))+blockHeight*i, blockWidth*3,1)
            oled.vline((left-(blockWidth//4))+(i*blockWidth),top-(blockHeight//4), blockWidth*3,1)
        ## วาดตัวเลขช่อง
        i = 0
        for r in range(3):
            for c in range(3):
                if ((r == (y>>yResponse)) and (c == (x>>yResponse))): # วาดกล่องสี่เหลี่ยมทึบ
                    oled.fill_rect(left-4+blockWidth*c,top-4+blockHeight*r,
                                   blockWidth, blockHeight,1)
                    oled.text(str(table[i]),left+blockWidth*c,top+blockHeight*r,0)
                else:
                    oled.text(str(table[i]),left+blockWidth*c,top+blockHeight*r,1)
                i+=1
        ## วาด
        oled.show()
        ## รับค่า
        (a,d,w,s,n) = getInput()
        #print(a,d,w,s,n)
        if (n):
            x2 = (x>>xResponse)
            y2 = (y>>yResponse)
            pos = (y2*3)+x2
            #print(x2,y2,pos)
            if (table[pos] == ""):
                table[pos] = "O"
                posX = x2
                posY = y2
                break
        ### Update value
        if (a):
            x-=1
        if (d):
            x+=1
        if (w):
            y-=1
        if (s):
            y+=1
        if (x < 0):
            x = 0
        if (y < 0):
            y = 0
        if (x > 2*(1<<xResponse)): # จำนวน￼ช่องคูณด้วย response
            x = 2*(1<<xResponse)
        if (y > 2*(1<<yResponse)): # จำนวน￼ช่องคูณด้วย response
            y = 2*(1<<yResponse)
        time.sleep_ms(20)

#######################################################
### Main program
#######################################################
doAgain = True
while doAgain:
    try:
        counter = 0
        while True:
            # รับค่า
            testControl2()
            drawTable()
            # ตรวจสอบว่าคนชนะ ?
            if (isWin("O")):
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
                    time.sleep_ms(200)
                    oled.invert(True)
                    time.sleep_ms(200)
                break
            # คอมพิวเตอร์เล่น
            while True:
                pos = random.getrandbits(8)%9 # สุ่ม 0..8
                if (table[pos] == ""): # ถ้ายังว่าง
                    table[pos] = "X"
                    break
            drawTable()
            # ตรวจสอบว่าคอมพิวเตอร์ชนะไหม?
            if (isWin("X")):
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
                    time.sleep_ms(200)
                    oled.invert(True)
                    time.sleep_ms(200)
                break
            # นับรอบการเล่น
            counter += 1
            if (counter == 4):
                break
    except KeyboardInterrupt:
        pass
    finally:
        for i in range(64):
            oled.scroll(0,-2)
            oled.show()
    doAgain = False
oled.poweroff()
