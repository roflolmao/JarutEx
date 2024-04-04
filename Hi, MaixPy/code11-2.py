# code11-2 - By: JarutEx - Fri Oct 16 2020
import sensor, image, time, lcd

lcd.init(freq=15000000)
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot() # Capture
    #process
    green_threshold = (0,   80,  -70,   -10,   -0,   30)
    blobs = img.find_blobs([green_threshold])
    if blobs:
        for b in blobs:
            tmp=img.draw_rectangle(b[0:4])
            tmp=img.draw_cross(b[5], b[6])
            c=img.get_pixel(b[5], b[6])
    #display
    lcd.display(img)
    print(clock.fps())
