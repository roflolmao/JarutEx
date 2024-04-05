# img1 - By: JarutEx - Mon Oct 4 2021

import lcd, image, time

lcd.freq(80000000)
lcd.init(color=(255,0,0))
clock = time.clock()
img = image.Image()

while(True):
    clock.tick()
    img.clear()
    img.draw_string(10,100,"JarutEx",(232,232,18),7)
    img.draw_string(10,20,"fps={}".format(clock.fps()),(252,252,252),2)
    lcd.display(img)
