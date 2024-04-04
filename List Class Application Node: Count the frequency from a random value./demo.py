# ต้องการสุ่มค่า 100 ชุด โดยใช้ตัวเลข 0-20 และนับความถี่
import random

data = []
freq = []
for i in range(100):
    item = random.getrandbits(5)%21
    if (len(data) == 0):
        data.append(item) # เก็บตัวเลขที่สุ่มได้
        freq.append(1) # เก็บค่าความถี่
    else:
        if (item in data):
            idx = data.index(item)
            freq[idx] += 1
        else:
            data.append(item) # เก็บตัวเลขที่สุ่มได้
            freq.append(1) # เก็บค่าความถี่
print("-------------------------")
print("\tData\tFreq.")
print("-------------------------")
sum = 0
for i in range(len(data)):
    print("{}\t{}\t{}".format(i+1,data[i],freq[i]))
    sum += freq[i]
print("-------------------------")
print("Freq. sum = {}".format(sum))
print("-------------------------")
