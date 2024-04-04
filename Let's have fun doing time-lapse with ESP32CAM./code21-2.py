# code21-2 time-laps
import machine as mc
import time
import camera
import os

camera.init(0,format=camera.JPEG)
camera.framesize(camera.FRAME_VGA)
camera.whitebalance(camera.WB_NONE)
sd = mc.SDCard()
time.sleep_ms(100)
if ('sd' in os.listdir()):
    os.umount('/sd')
os.mount(sd, '/sd')
frameCounter = 0
for i in range(100):
    frameCounter += 1
    buf = camera.capture()
    fname = "/sd/{:04d}.jpg".format(frameCounter)
    f = open(fname, 'w')
    f.write(buf)
    time.sleep_ms(100)
    f.close()
    print("Frame No.{}".format(frameCounter))
    time.sleep_ms(1000)
sd.deinit()
camera.deinit()
