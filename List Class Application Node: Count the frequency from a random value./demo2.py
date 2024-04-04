# ต้องการสุ่มค่า 100 ชุด โดยใช้ตัวเลข 0-20 และนับความถี่
import random

data = []
freqTable = []
# random 100 items
for i in range(100):
    data.append(random.getrandbits(5)%21)
# processing
data.sort()
freqTableIdx = 0
for i in range(100):
    if (i == 0): # first time
        freqTable.append([data[i],1])
    else:
        if (freqTable[freqTableIdx][0] == data[i]):
            freqTable[freqTableIdx][1] += 1
        else:
            freqTable.append([data[i],1])
            freqTableIdx += 1
print("-------------------------")
print("\tData\tFreq.")
print("-------------------------")
sum = 0
for i in range(len(freqTable)):
    print("{}\t{}\t{}".format(i+1, freqTable[i][0],freqTable[i][1]))
    sum += freqTable[i][1]
print("Freq. sum = {}".format(sum))
print("-------------------------")
