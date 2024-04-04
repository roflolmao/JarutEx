# code16-1 : MMA7660FC with Raspberry Pi
import time
import smbus
import sys
if sys.platform != 'linux':
    sys.exit(1)
i2c = smbus.SMBus(1)
class MMA7660FC:
    def __init__(self, i2c, addr=0x4c):
        self.i2c = i2c
        self.mma7660fcAddr = addr
        self.i2c.write_byte_data( self.mma7660fcAddr, 0x07, 0x01 )
        self.i2c.write_byte_data( self.mma7660fcAddr, 0x08, 0x07 )
        time.sleep(0.01)
    def read(self):
        data = self.i2c.read_i2c_block_data(self.mma7660fcAddr, 0x00, 3)
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

if __name__=='__main__':
    sensor = MMA7660FC(i2c)
    while True:
        sData = sensor.read()
        print("Acceleration ({},{},{})".format(sData[0],sData[1],sData[2] ))
        time.sleep(1)
