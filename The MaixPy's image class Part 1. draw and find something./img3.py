# img3 - By: JarutEx - Mon Oct 4 2021

import lcd, image, time, gc, machine
import random

gc.enable()
gc.collect()

lcd.freq(80000000)
lcd.init(color=(255,0,0))
img = image.Image()

fLines = None
gc.collect()
img.clear()
for i in range(1+random.getrandbits(4)):
    img.draw_circle( random.getrandbits(7)+20, random.getrandbits(7)+20,
    random.getrandbits(4)+4, (255,255,255), 1)
fCircles = img.find_circles((0,0,img.width(),img.height()))
nCircles = len(fCircles)
if (nCircles > 0):
    for i in range(nCircles):
        print("{}".format(fCircles[i]))
lcd.display(img)
time.sleep(5)
fCircles = None
img = None
lcd.deinit()
gc.collect()
machine.reset()

img.draw_circle(x,y,r,(rr,gg,bb),2,(rr,gg,bb))
