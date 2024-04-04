# code15-1
import time
import gc
import machine as mc
from machine import I2C, Pin

gc.enable()
gc.collect()
sclPin = mc.Pin(5)
sdaPin = mc.Pin(4)
i2c = mc.I2C(scl=sclPin,sda=sdaPin,freq=2000000)
print("i2c device(s) address = {}".format(i2c.scan()))

class MMA7660FC:
    def __init__(self, i2c, addr=0x4c):
        self.i2c = i2c
        self.mma7660fcAddr = addr
        mma7660fcBuffer = bytearray(2)
        # Active mode
        mma7660fcBuffer[0] = 0x07
        mma7660fcBuffer[1] = 0x01
        self.i2c.writeto(self.mma7660fcAddr, mma7660fcBuffer)
        # 1 Sample/second active
        mma7660fcBuffer[0] = 0x08
        mma7660fcBuffer[1] = 0x07
        self.i2c.writeto(self.mma7660fcAddr, mma7660fcBuffer)
        time.sleep_ms(10)

    def read(self):
        data = self.i2c.readfrom(self.mma7660fcAddr,3) # 0x00, 3)
             
        # Convert the data to 6-bits
        xAccl = data[0] & 0x3F
        if xAccl > 31 :
            xAccl -= 64
        yAccl = data[1] & 0x3F
        if yAccl > 31 :
            yAccl -= 64
        zAccl = data[2] & 0x3F
        if zAccl > 31 :
            zAccl -= 64
        return (xAccl,  yAccl,  zAccl)

# Output data to screen
sensor = MMA7660FC(i2c)
while True:
    sensorData = sensor.read()
    print("Acceleration ({},{},{})".format(sensorData[0],sensorData[1],sensorData[2] ))
    time.sleep_ms(50)
