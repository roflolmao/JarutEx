# img2 - By: JarutEx - Mon Oct 4 2021

import lcd, image, time, gc, machine

gc.enable()
gc.collect()

lcd.freq(80000000)
lcd.init(color=(255,0,0))
img = image.Image()

fLines = None
gc.collect()
img.clear()
img.draw_line( 10, 10, 200, 100, coloe=(255,255,255))
fLines = img.find_lines((0,0,img.width(),img.height()))
nLines = len(fLines)
if (nLines > 0):
    img.draw_string(10,10,"lines={}".format(nLines),(8,242,232),2)
    for i in range(nLines):
        print("{}".format(fLines[i]))
lcd.display(img)
time.sleep(2)
fLines = None
img = None
lcd.deinit()
gc.collect()
machine.reset()
