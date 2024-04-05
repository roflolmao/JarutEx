# lcd1.py - By: JarutEx - Sat Oct 2 2021

import lcd,time,sensor

if (lcd.type() == 0):
    print("Error : no lcd shield!")
    while (True):
        pass

lcd.freq(16000000)
lcd.init(color=(255,0,0))
colors = [
    lcd.BLACK,
    lcd.NAVY,
    lcd.DARKGREEN,
    lcd.DARKCYAN,
    lcd.MAROON,
    lcd.PURPLE,
    lcd.OLIVE,
    lcd.LIGHTGREY,
    lcd.DARKGREY,
    lcd.BLUE,
    lcd.GREEN,
    lcd.CYAN,
    lcd.RED,
    lcd.MAGENTA,
    lcd.YELLOW,
    lcd.WHITE,
    lcd.ORANGE,
    lcd.GREENYELLOW,
    lcd.PINK
]
lcd.set_backlight(True)
for color in colors:
    lcd.clear(color)
    lcd.draw_string(40,100,"JarutEx",lcd.WHITE,color)
    lcd.draw_string(40,120,"JarutEx",lcd.BLACK,color)
    time.sleep(1)
lcd.clear(lcd.RED)
lcd.rotation(0)
lcd.draw_string(30, 30, "JarutEx", lcd.WHITE, lcd.RED)
time.sleep(1)
lcd.rotation(1)
lcd.draw_string(60, 60, "JarutExy", lcd.WHITE, lcd.RED)
time.sleep(1)
lcd.rotation(2)
lcd.draw_string(120, 60, "JarutEx", lcd.WHITE, lcd.RED)
time.sleep(1)
lcd.rotation(3)
lcd.draw_string(120, 120, "JarutExy", lcd.WHITE, lcd.RED)
time.sleep(1)
if (lcd.get_backlight()):
    lcd.set_backlight( False )
