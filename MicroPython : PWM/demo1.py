#fade LED
from machine import Pin,PWM
import time

led = PWM(Pin(2))
led.freq(50)
led.duty(1023)
for i in range(0,1023):
    #print(i)
    led.duty(1023-i)
    time.sleep_ms(1)
for i in range(0,1024):
    #print(i)
    led.duty(i)
    time.sleep_ms(1)
led.deinit()
led = Pin(2)
led.value(0)
