import time
from machine import Pin,PWM
spk = PWM(Pin(13))
spk.duty(0)
for i in range(100,1000,200):
    spk.freq(i)
    time.sleep_ms(20)
spk.duty(1023)
spk.deinit()
spk = Pin(13)
spk.value(1)

เมื่อนำส่วนของการทำงานมาเขียนเป็นฟังก์ชัน​beep() สามารถเขียนได้ดังนี้

def beep(f,d=512):
    spk = PWM(Pin(13),freq=f, duty=d)
    spk.init()
    time.sleep_ms(50)
    spk.deinit()
