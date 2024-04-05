import pyb
import math
import sys
from pyb import Pin

usb = pyb.USB_VCP()
usb.write("Hello, I'm {}\n".format(sys.platform))
usb.write("Press [UKEY] to exit!\n")

sw = Pin('PA0', Pin.IN)
while not (1-sw.value()):
    pyb.delay(20)
usb.write("End of Program.")
