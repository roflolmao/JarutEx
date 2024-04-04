# code13-1
import sys
import gc
import os
import esp
import time
import math
import machine as mc
from kjlcd import LCD
scl_pin = mc.Pin(5)
sda_pin = mc.Pin(4)
i2c = mc.I2C(scl=scl_pin,sda=sda_pin)
lcd_addr= const(0x27)
lcd = LCD(i2c,lcd_addr)
lcd.goto(0,0)
lcd.puts("{}[{}]".format(sys.platform,esp.flash_size()))
lcd.goto(0,1)
lcd.puts("(C)2020,JarutEx")
