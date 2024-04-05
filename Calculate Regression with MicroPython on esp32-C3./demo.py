###########################################################
# calculate regression
# jarutex.com
###########################################################
import gc
import time as tm
import machine as mc
from machine import Pin,ADC,I2C
from ssd1306 import SSD1306_I2C

###########################################################
# setting
###########################################################
gc.enable()
gc.collect()

mc.freq(160000000)

pinScl = Pin(10)
pinSda = Pin(9)

i2c = I2C(0,scl=pinScl,sda=pinSda,freq=800000)
oled_addr = const(0x3c)
oled = SSD1306_I2C(128,64,i2c)

x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
y = [29.5,29.2,29.0,28.9,28.6,28.8,28.5,28.3,29.0,29.6,30.8,31.8,31.7,32.1,32.5,31.6,30.5,30.5,30.2,29.6,29.5,29.2,28.1,28.9]
n = len(x)
sumX = 0.0
sumY = 0.0
sumX2 = 0.0
sumY2 = 0.0
sumXY = 0.0

###########################################################
# start
###########################################################
oled.poweron()
oled.init_display()
oled.fill(1)
oled.text("JarutEx", 10, 10, 0)
oled.show()

###########################################################
# main program
###########################################################
#
# calculate
#
for i in range(len(x)):
    sumXY = (sumXY+(x[i]*y[i]))
    sumX2 = (sumX2+(x[i]*x[i]))
    sumY2 = (sumY2+(y[i]*y[i]))
    sumX = (sumX+x[i])
    sumY = (sumY+y[i])
a = ((sumY*sumX2)-(sumX*sumXY))/((n*sumX2)-(sumX*sumX))
b = ((n*sumXY)-(sumX*sumY))/((n*sumX2)-(sumX*sumX))
#
# draw axis
#
oled.fill(0)
posx = 0
posy = 0
for i in range(25):
    if ((i % 8)==0):
        oled.text("{}".format(i),8+posx*36,56)
        posx+=1
for posy in range(64):
    oled.pixel(4,posy,1)
for posx in range(128):
    oled.pixel(posx,54,1)
oled.show()
#
# point (x,y)
#
for posx in range(n):
    print(posx*5+8,int(y[posx]))
    oled.text("+",8+posx*5,int(y[posx]))
    #oled.pixel(posx*5+8,int(y[posx]),1)
oled.show()
#
# draw Y = a + bX + c
#
for posx in range(8,124,1):
    posy = a+b*posx
    oled.pixel(posx,int(posy),1)
    
oled.show()
tm.sleep_ms(10000)

###########################################################
# end of program
###########################################################
oled.fill(0)
oled.show()
oled.poweroff()
