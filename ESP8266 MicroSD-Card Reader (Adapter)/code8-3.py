# code8-3
import json
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
# สร้างตัวแปร dictionary เก็บข้อมูล
devices = {}
devices['id'] = 1
devices["board"] = "esp8266"
devices["ios"] = [{4:"sda",5:"scl",12:"MISO",13:"MOSI",14:"SCK",15:"CS"}]
# แปลงข้อมูล dictionary เป็น string
myProject = json.dumps(devices) 
# เขียน myProject ลง SD-Card
me = open('/sd/me.json','w')
me.write(myProject)
me.close()
# อ่านข้อมูลจากไฟล์
me = open('/sd/me.json','r')
text = me.read()
me.close()
# แปลงเป็น dictionary
data = json.loads(text)
# แสดงผล
print(data)
#สิ้นสุดการทำงาน
# ยกเลิกการเชื่อมต่อกับการ์ด
os.umount('/sd')
# ยกเลิกการใช้พอร์ต SPI
spi.deinit()
