# JarutEx I2C Character LCD Library
import time
class LCD():
    MASK_RS = const(0x01)
    MASK_RW = const(0x02)
    MASK_E = const(0x04)
    SHIFT_BACKLIGHT = const(3)
    SHIFT_DATA = const(4)
    def __init__(self, i2c, lcd_addr=0x38):
        self.lcd_bl = True
        self.lcd_addr = lcd_addr
        self.i2c = i2c
        self.reset()
    def reset(self):
        time.sleep_ms(250)
        self.cmd(0x33)
        self.cmd(0x32)
        self.cmd(0x06)
        self.cmd(0x0C)
        self.cmd(0x28)
        self.cmd(0x01)
        time.sleep_ms(500)
        self.backlight()
    def write(self, value):
        buffer = bytearray(1)
        buffer[0] = value & 0xff
        self.i2c.writeto(self.lcd_addr, buffer)
    def cmd(self,byte):
        high_nib = (byte & 0xF0)|(self.lcd_bl << SHIFT_BACKLIGHT)
        low_nib = ((byte<<4) & 0xF0)|(self.lcd_bl << SHIFT_BACKLIGHT)
        self.write(high_nib|MASK_E)
        self.write(high_nib)
        self.write(low_nib|MASK_E)
        self.write(low_nib)
    def data(self,byte):
        high_nib = (byte & 0xF0)|MASK_RS|(self.lcd_bl << SHIFT_BACKLIGHT)
        low_nib = ((byte<<4) & 0xF0)|MASK_RS|(self.lcd_bl << SHIFT_BACKLIGHT)
        self.write(high_nib|MASK_E)
        self.write(high_nib)
        self.write(low_nib|MASK_E)
        self.write(low_nib)
    def backlight(self,status=True):
        if status:
            self.write(1<<SHIFT_BACKLIGHT)
            self.lcd_bl = True
        else:
            self.write(0)
            self.lcd_bl = False
    def goto(self,x,y):
        if y==1:
            pos = 0xC0
        else:
            pos = 0x80
        self.cmd(pos|x)
    def putc(self,ch):
        self.data(ord(ch))
    def puts(self,s):
        for idx in range(len(s)):
          self.putc(s[idx])
