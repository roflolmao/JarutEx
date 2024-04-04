# เราจะหาข้อมูลลำดับที่ n จากลิสต์ได้อย่างไร?
import random
# 1 สุ่มตัวเลข
data = []
for i in range(20):
    data.append(random.randint(0,16))
# 2 เรียงข้อมูล
print("Raw data ........: {}".format(data))
data.sort()
print("Sorted ..........: {}".format(data))
# 3 สร้างลิสต์ใหม่ที่ไม่เก็บข้อมูลซ้ำกัน
newData = []
for i in range(len(data)):
    if data[i] not in newData:
        newData.append( data[i] )
print("New list ........: {}".format(newData))
# 4-5 find
n = int(input("data?"))
if (n in range(1, len(newData)+1)):
    print(newData[n-1])
else:
    print("{} : Out of range!".format(n))
