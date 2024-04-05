#######################################################
### sprite
### board: ML4M
### (C) 2021, JarutEx
#######################################################
from machine import Pin,I2C,ADC, DAC
import math
import machine
import gc
import ssd1306
import random
import time
import sys
import framebuf
from framebuf import FrameBuffer


#######################################################
gc.enable()
gc.collect()
machine.freq(240000000)

#######################################################
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

#######################################################
swA = Pin(32, Pin.IN)
swB = Pin(33, Pin.IN)
swC = Pin(34, Pin.IN, Pin.PULL_UP) # select
swD = Pin(35, Pin.IN) # start
jst = (ADC(Pin(39)), ADC(Pin(36))) # X,Y
jst[0].width( ADC.WIDTH_12BIT ) # 12bit
jst[0].atten( ADC.ATTN_11DB ) # 3.3V
jst[1].width( ADC.WIDTH_12BIT ) # 12bit
jst[1].atten( ADC.ATTN_11DB ) # 3.3V

#######################################################
actor = [
    FrameBuffer(bytearray([
        0b00000000,
        0b00001000,
        0b00011000,
        0b00111000,
        0b11111000,
        0b00111000,
        0b00011000,
        0b00001000
    ]),8,8,framebuf.MONO_HLSB),
    FrameBuffer(bytearray([
        0b00000000,
        0b00100000,
        0b00110000,
        0b00111000,
        0b00111110,
        0b00111000,
        0b00110000,
        0b00100000
    ]),8,8,framebuf.MONO_HLSB),
    FrameBuffer(bytearray([
        0b00000000,
        0b00010000,
        0b00010000,
        0b00111000,
        0b01111100,
        0b11111110,
        0b00000000,
        0b00000000
    ]),8,8,framebuf.MONO_HLSB),
    FrameBuffer(bytearray([
        0b00000000,
        0b00000000,
        0b11111110,
        0b01111100,
        0b00111000,
        0b00010000,
        0b00010000,
        0b00000000
    ]),8,8,framebuf.MONO_HLSB)
]
scrWidth = 128
scrHeight = 64
actorSize = (8,8)
actorPos = [scrWidth//2-4,scrHeight//2-4]
actorDir = 0 #0,1,2,3:left,right,up,down

flag = FrameBuffer(bytearray([
0b01000000,
0b01111111,
0b01111110,
0b01110000,
0b01000000,
0b01000000,
0b01100000,
0b11110000
]),8,8,framebuf.MONO_HLSB)
flagPos = [0,0]

wall = FrameBuffer(bytearray([
    0b00011110,
    0b11100011,
    0b01000001,
    0b10000010,
    0b01000001,
    0b10000010,
    0b10000001,
    0b01111110
]),8,8,framebuf.MONO_HLSB)

maze = [
    0b1111000111111101,
    0b1000010000100101,
    0b0011000100000101,
    0b1001001110010101,
    0b1000001000010001,
    0b1011110010111011,
    0b0001000010000001,
    0b110001100011111
]

#######################################################
def beep():
    spkPin.write(255)
    time.sleep_ms(20)
    spkPin.write(0)
    
#######################################################
def getInput():
    left = False
    right = False
    up = False
    down = False
    button1 = False
    button2 = False
    button3 = False
    button4 = False
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
    c = 1-swC.value()
    d = swD.value()
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
    if (c):
        t0 = time.ticks_ms()
        time.sleep_ms(25)
        c2 = swC.value()
        if (c == c2):
            button3 = True
    if (d):
        t0 = time.ticks_ms()
        time.sleep_ms(25)
        d2 = swD.value()
        if (d == d2):
            button4 = True
    return (left,right,up,down,button1, button2, button3, button4)

#######################################################
def drawMaze():
    for r in range(8):
        mask = 0b1000000000000000
        for c in range(16):
            if (maze[r] & mask):
                oled.blit(wall,c*8, r*8)
            mask >>= 1
    oled.blit(flag, flagPos[0],flagPos[1])

#######################################################
def randFlag():
    while True:
        r = random.getrandbits(3) # 0..7
        c = random.getrandbits(4) # 0..15
        mask = (0b1000000000000000 >> c)
        if (maze[r] & mask):
            pass
        else:
            flagPos[0] = c*8
            flagPos[1] = r*8
            break
    
#######################################################
def randActor():
    while True:
        r = random.getrandbits(3) # 0..7
        c = random.getrandbits(4) # 0..15
        mask = (0b1000000000000000 >> c)
        if (maze[r] & mask):
            pass
        else:
            if ((c*8 != flagPos[0]) and (r*8 != flagPos[1])): # ต้องไม่ใช่ที่เดียวกับธง
                actorPos[0] = c*8
                actorPos[1] = r*8
                break
            

#######################################################
def isWall(c,r):
    c //= 8
    r //= 8
    mask = (0b1000000000000000 >> c)
    if (maze[r] & mask):
        return True
    return False

#######################################################
### Main program
#######################################################
beep()
try:
    randFlag()
    randActor()
    while True:
        (l,r,u,d,a,b,m1,m2)=getInput()
        if (m1):
            break
        if (a):
            randFlag()
        if (b):
            randActor()
        if (l):
            actorDir = 0
            if (actorPos[0] > 0):
                if (isWall(actorPos[0]-actorSize[0],actorPos[1])):
                    beep()
                else:
                    actorPos[0] -= actorSize[0]

        if (r):
            actorDir = 1
            if (actorPos[0] < scrWidth-actorSize[0]):
                if (isWall(actorPos[0]+actorSize[0],actorPos[1])):
                    beep()
                else:
                    actorPos[0] += actorSize[0]

        if (u):
            actorDir = 2
            if (actorPos[1] > 0):
                if (isWall(actorPos[0],actorPos[1]-actorSize[1])):
                    beep()
                else:
                    actorPos[1] -= actorSize[1]
    
        if (d):
            actorDir = 3
            if (actorPos[1] < scrHeight-actorSize[1]):
                if (isWall(actorPos[0],actorPos[1]+actorSize[1])):
                    beep()
                else:
                    actorPos[1] += actorSize[1]

        oled.fill(0)
        drawMaze()
        oled.blit(actor[actorDir], actorPos[0], actorPos[1])
        oled.show()
        time.sleep_ms(100)
except KeyboardInterrupt:
    pass
beep()
oled.poweroff()
