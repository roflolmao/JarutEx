#code21-1
import camera
import machine
import os
import time

camera.init(0,format=camera.JPEG)
camera.framesize(camera.FRAME_VGA)
camera.whitebalance(camera.WB_NONE) 
camera.saturation(0)
camera.brightness(0)
camera.contrast(0)
camera.quality(10)

sd = machine.SDCard()

time.sleep_ms(100)
os.mount(sd, '/sd')
buf = camera.capture()
f = open('/sd/capture.jpg', 'w')
f.write(buf)
time.sleep_ms(100)
f.close()
sd.deinit()
camera.deinit()
