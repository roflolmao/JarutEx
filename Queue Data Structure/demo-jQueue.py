# demo-jQueue.py
from jQueue import Queue
from st7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import machine as mc
import time
import math
import esp32

mc.freq(240000000)
spi = SPI(2, baudrate=27000000,
          sck=Pin(14), mosi=Pin(12),
          polarity=0, phase=0)
# dc, rst, cs
tft=TFT(spi,15,13,2)
tft.init_7735(tft.GREENTAB80x160)
tft.fill(TFT.BLACK)
dataQ = Queue(160)
for i in range(160):
    dataQ.push(0)
while True:
    tft.fill(TFT.BLACK)
    # input
    tf = esp32.raw_temperature()
    tc = int((tf-32.0)/1.8)
    # process
    dataQ.pop()
    dataQ.push(tc)
    # show
    for i in range(160):
        value = dataQ.items[i]
        if value >= 49:
            tft.vline((i,80-value), value, TFT.RED)
        else:
            tft.vline((i,80-value), value, TFT.GREEN)
    time.sleep_ms(1000)
