######################################################################
#
# MCP4922 12-bit ADC with SPI Interface
# 
# (C) 2021, JarutEx
#     https://www.jarutex.com
######################################################################
from machine import SPI, Pin, ADC
import time

spi = SPI(1,baudrate=20000000,sck=Pin(18,Pin.OUT),mosi=Pin(23,Pin.OUT),miso=Pin(19,Pin.IN))
pinCS = Pin(27, Pin.OUT)
pinCS.on()

try:
    dacData = 0
    dacDir = 0
    while True:
        dacData = 4000
        x2 = ((dacData & 0b0000111111111111) | 0b0111000000000000)
        buffer = x2.to_bytes(2,'big')
        pinCS.off()
        spi.write(buffer)
        pinCS.on()
        time.sleep_ms(500)
        dacData = 100
        x2 = ((dacData & 0b0000111111111111) | 0b0111000000000000)
        buffer = x2.to_bytes(2,'big')
        pinCS.off()
        spi.write(buffer)
        pinCS.on()
        time.sleep_ms(500)
except KeyboardInterrupt:
    pass
tmr0.deinit()
spi.deinit()
