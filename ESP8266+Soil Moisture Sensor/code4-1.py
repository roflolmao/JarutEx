import time
from machine import ADC
pinAdc = ADC(0)
while True:
    dValue = pinAdc.read()
    print(dValue)
    time.sleep_ms(1000)
