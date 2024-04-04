#######################################################
### Tic-Tac-Toe
#######################################################
from machine import Pin,I2C
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
screenWidth = 128
screenHeight = 64

table = [1,2,3,4,5,6,7,8,9]

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
### Main program
counter = 0
while True:
    # วาดตาราง
    drawTable()
    # รับค่า
    print("Human")
    while True:
        try:
            pos = int(input("ตำแหน่งที่ต้องการเลือก(1-9)?"))
        except:
            print("กรุณากรอก 1..9")
        if ((pos < 1) or (pos > 9)):
             print("กรุ่ณากรอก 1..9")
        else:
             if (table[pos-1] != pos):
                 print("กรุณาเลือกช่องอื่น")
             else:
                 table[pos-1] = "O"
                 break
    drawTable()
    # ตรวจสอบว่าคนชนะ ?
    if (isWin("O")):
        print("ขอแสดงความยินด้วยที่คุณชนะ")
        break
    # คอมพิวเตอร์เล่น
    print("Computer:")
    while True:
        pos = random.getrandbits(8)%9 # สุ่ม 0..8
        if (table[pos] == (pos+1)): # ถ้ายังว่าง
            table[pos] = "X"
            break
    # ตรวจสอบว่าคอมพิวเตอร์ชนะไหม?
    if (isWin("X")):
        print("ขอแสดงความเสียใจกับความพ่ายแพ้ของคุณ!")
        break
    # นับรอบการเล่น
    counter += 1
    if (counter == 4):
        break
drawTable()
time.sleep_ms(2000)
oled.poweroff()
