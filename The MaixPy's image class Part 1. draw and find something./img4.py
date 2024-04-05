# img4 - By: JarutEx - Mon Oct 4 2021

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
    img.draw_rectangle(
        random.getrandbits(8),random.getrandbits(8),
        4+random.getrandbits(6),4+random.getrandbits(6),
        (random.getrandbits(8),random.getrandbits(8),random.getrandbits(8)),
        random.getrandbits(2)+1,
        True)
fRects = img.find_rects((0,0,img.width(),img.height()))
nRects = len(fRects)
if (nRects > 0):
    for i in range(nRects):
        print("{}".format(fRects[i]))
lcd.display(img)
time.sleep(5)
fRects = None
img = None
lcd.deinit()
gc.collect()
machine.reset()
