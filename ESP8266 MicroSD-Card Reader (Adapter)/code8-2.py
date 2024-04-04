# code8-2
import json
# สร้างตัวแปร dictionary เก็บข้อมูล
devices = {}
devices['id'] = 1
devices["board"] = "esp8266"
devices["ios"] = [{4:"sda",5:"scl",12:"MISO",13:"MOSI",14:"SCK",15:"CS"}]
# แปลงข้อมูล dictionary เป็น string
myProject = json.dumps(devices) 
print("myProject type:{},value:{}".format(type(myProject), myProject))
# แปลงสตริงกลับไปเป็น dictionary
data = json.loads(myProject)
print("data type:{},value:{}".format(type(data),data))
