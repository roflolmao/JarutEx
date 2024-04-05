# lcd2 - By: JaritEx - Sun Oct 3 2021

import image, time, lcd

clock = time.clock()
print("lcd freq. = {}Hz".format(lcd.freq()))
lcd.freq(80000000)
lcd.init(color=(255,0,0))
img = image.Image("/sd/pmai.jpg")

while(True):
    clock.tick()
    lcd.display(img)
