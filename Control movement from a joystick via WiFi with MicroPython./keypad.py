########################################################################################
# keypad.py
# เป้าหมาย สร้างอุปกรณ์ใช้ Game Pad Controller แบบไร้สาย
# ผู้พัฒนา JarutEx
# 2021-09-02 ปรับปรุงเรื่อง JoyStick
# 2021-08-20 สร้างคลาส Keypad ให้รองรับ JoyStick และปุ่ม A,B,C,D,E,F ยกเว้นปุ่มที่จอยสติก
#
########################################################################################
from machine import Pin, ADC

########################################################################################
class Keypad:
    def __init__(self):
        self.swA = Pin(32, Pin.IN)
        self.swB = Pin(33, Pin.IN)
        self.swC = Pin(35, Pin.IN)
        self.swD = Pin(34, Pin.IN)
        self.swF = Pin(26, Pin.IN) # select
        self.swE = Pin(27, Pin.IN) # start
        self.jst = (ADC(Pin(36)), ADC(Pin(39))) # X,Y
        self.jst[0].width( ADC.WIDTH_12BIT ) # 12bit
        self.jst[0].atten( ADC.ATTN_11DB ) # 3.3V
        self.jst[1].width( ADC.WIDTH_12BIT ) # 12bit
        self.jst[1].atten( ADC.ATTN_11DB ) # 3.3V
        self.bits = 0x000 # 10-bits
        self.x = self.jst[0].read()
        self.y = 4095-self.jst[1].read()
        self.a = self.swA.value()
        self.b = self.swB.value()
        self.c = self.swC.value()
        self.d = self.swD.value()
        self.e = self.swE.value()
        self.f = self.swF.value()
    def read(self):
        self.x = self.jst[0].read()
        self.y = 4095-self.jst[1].read()
        self.a = self.swA.value()
        self.b = self.swB.value()
        self.c = self.swC.value()
        self.d = self.swD.value()
        self.e = self.swE.value()
        self.f = self.swF.value()
    def show(self):
        self.read()
        print("{} ({},{}) SWs: A{} B{} C{} D{} E{} F{}".format(
            hex(self.status()),
            self.x,self.y,
            self.a,self.b,self.c,self.d,self.e,self.f))
    def status(self):
        self.bits = 0x000 # 10-bits
        if (self.x < 1500): # left
            self.bits = self.bits | 0x400
        elif (self.x > 2500): # right
            self.bits = self.bits | 0x200
        if (self.y < 1500): # up
            self.bits = self.bits | 0x080
        elif (self.y > 2500): # down
            self.bits = self.bits | 0x040
        if (self.a == 0):
            self.bits = self.bits | 0x020
        if (self.b == 0):
            self.bits = self.bits | 0x010
        if (self.c == 0):
            self.bits = self.bits | 0x008
        if (self.d == 0):
            self.bits = self.bits | 0x004
        if (self.e == 0):
            self.bits = self.bits | 0x002
        if (self.f == 0):
            self.bits = self.bits | 0x001
        return self.bits
