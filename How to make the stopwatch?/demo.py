from ST7735 import TFT
import machine as mc
from machine import SPI,Pin, Timer
import time
import math

#################################################################
###### setting ##################################################
#################################################################
mc.freq(240000000)
spi = SPI(2, baudrate=26000000,
          sck=Pin(14), mosi=Pin(12),
          polarity=0, phase=0)
sw = Pin(0, Pin.IN, Pin.PULL_UP)
# dc, rst, cs
tft=TFT(spi,15,13,2)
tft.fill(tft.BLACK)
tft.swap()
screenCenterX = 40
screenCenterY = 40
second = 0
minute = 0
hour = 0
state = 0

#################################################################
###### sub modules ##############################################
#################################################################
def midPointCircleDraw(x_centre, y_centre, r, c):
    x = r
    y = 0

    tft.setPixel(x + x_centre,y + y_centre, c)

    # When radius is zero only a single
    # point be printed
    if (r > 0) :
        tft.setPixel(x + x_centre,-y + y_centre, c)
        tft.setPixel(y + x_centre,x + y_centre, c)
        tft.setPixel(-y + x_centre,x + y_centre, c)
     
    # Initialising the value of P
    P = 1 - r
 
    while x > y:
        y += 1
         
        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1
             
        # Mid-point outside the perimeter
        else:        
            x -= 1
            P = P + 2 * y - 2 * x + 1
         
        # All the perimeter points have
        # already been printed
        if (x < y):
            break
         
        # Printing the generated point its reflection
        # in the other octants after translation
        tft.setPixel(x + x_centre,y + y_centre, c)
        tft.setPixel(-x + x_centre, y + y_centre, c)
        tft.setPixel( x + x_centre,-y + y_centre, c)
        tft.setPixel( -x + x_centre,-y + y_centre, c)
         
        # If the generated point on the line x = y then
        # the perimeter points have already been printed
        if x != y:
            tft.setPixel(y + x_centre, x + y_centre, c)
            tft.setPixel(-y + x_centre, x + y_centre, c)
            tft.setPixel(y + x_centre, -x + y_centre, c)
            tft.setPixel(-y + x_centre, -x + y_centre, c)

def rotate(pX,pY,angle):
    rad = math.radians(angle)
    pX -= screenCenterX
    pY -= screenCenterY
    xCos = pX*math.cos(rad)
    ySin = pY*math.sin(rad)
    xSin = pX*math.sin(rad)
    yCos = pY*math.cos(rad)
    newX = xCos - ySin + screenCenterX
    newY = xSin + yCos + screenCenterY
    return (int(newX), int(newY))

def drawClock():
    midPointCircleDraw(screenCenterX, screenCenterY, 39, tft.color(232,232,232))
    n12x = screenCenterX
    n12y = 2
    n12y2 = 8
    for i in range(12):
        newX,newY = rotate( n12x, n12y, 30*i)
        newX2,newY2 = rotate( n12x, n12y2, 30*i)
        tft.line((newX,newY),(newX2, newY2),tft.color(232, 232, 64))
        
def drawSecond( sec ):
    deg = sec*6
    n12x = screenCenterX
    n12y = 10
    newX,newY = rotate( n12x, n12y, deg)
    tft.line((screenCenterX, screenCenterY), (newX, newY), tft.color(232, 64, 232))

def cbSecond(x):
    global second, minute, hour
    second += 1
    if (second == 60):
        second = 0
        minute += 1
        if (minute == 60):
            minute = 0
            hour += 1
            if (hour == 12):
                hour = 0
    tft.fill(tft.BLACK)
    drawClock()
    drawSecond(second)
    tft.swap()
    
#################################################################
###### main program #############################################
#################################################################
tft.fill(tft.BLACK)
drawClock()
drawSecond(0)
tft.swap()
secTmr = Timer(0)
while True:
    if (sw.value()==0):
        if state == 0:
            secTmr.init( period=1000, mode=Timer.PERIODIC, callback=cbSecond)
            state = 1 # start
        else:
            state = 0
            secTmr.deinit()
            tft.fill(tft.BLACK)
            drawClock()
            drawSecond(0)
            tft.text("H:{}".format(hour),(96,24),tft.color(232, 192, 194))
            tft.text("M:{}".format(minute),(96,34),tft.color(192, 232, 194))
            tft.text("S:{}".format(second),(96,44),tft.color(194, 192, 232))
            tft.swap()
            second = 0
            minute = 0
            hour = 0
        time.sleep(0.25)
