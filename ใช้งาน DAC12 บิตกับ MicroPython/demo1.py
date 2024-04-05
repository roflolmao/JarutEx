######################################################################
#
# MCP4922 12-bit ADC with SPI Interface
# 
# (C) 2021, JarutEx
#     https://www.jarutex.com
######################################################################
from machine import SPI, Pin, ADC
import time

pinCS = Pin(27, Pin.OUT)
pinCS.on()

spi = SPI(1,baudrate=20000000,sck=Pin(18,Pin.OUT),mosi=Pin(23,Pin.OUT),miso=Pin(19,Pin.IN))

try:
    dacData = 0
    dacDir = 0
    while True:
        x2 = 0b0111000000000000
        x2 |= (dacData & 0b0000111111111111) 
        buffer = x2.to_bytes(2,'big')
        pinCS.off()
        spi.write(buffer)
        pinCS.on()
        if (dacDir):
            dacData -= 1
            if (dacData < 0):
                dacData = 1
                dacDir = 0
        else:
            dacData += 1
            if (dacData > 4095):
                dacData = 4094
                dacDir = 1
        time.sleep_us(10)
except KeyboardInterrupt:
    pass
tmr0.deinit()
spi.deinit()
