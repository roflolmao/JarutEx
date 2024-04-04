#code8-1 : list
import sdcard, os
from machine import Pin, SPI
# กำหนดขา CS
sdCSPin = Pin(15)
# เลือกใช้ SPI พอร์ต 1
spi = SPI(1)
# สร้างวัตถุ sdcard
sd = sdcard.SDCard(spi, sdCSPin)
# เชื่อมต่อการ์ดเข้ากับโฟลเดอร์ /sd
os.mount(sd, '/sd')
# อ่านรายการไฟล์ในโฟลเดอร์ /sd
listFiles = os.listdir('/sd')
if len(listFiles) > 0:
    print("{file(s) in /sd}".format(listFiles))
else:
    print("no file!")
# ยกเลิกการเชื่อมต่อกับการ์ด
os.umount('/sd')
# ยกเลิกการใช้พอร์ต SPI
spi.deinit()
