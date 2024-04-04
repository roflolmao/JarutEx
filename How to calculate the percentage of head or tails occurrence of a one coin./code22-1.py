#code22-1
import random
def randCoin():
    return int(random.random()*2)
def calcPercentage(m, n):
    if n == 0:
        return 0
     return (100.0*(m/n))
numH = 0
numT = 0
try:
    n = int(input("จำนวนครั้งการสุ่ม?"))
    for counter in range(n):
        if (randCoin()==0):
             numH += 1
         else:
             numT += 1
     print("H={}%, T={}%".format(
                calcPercentage(numH), 
                calcPercentage(numT)))
except:
    print("กรุณากรอกจำนวนครั้งเป็นตัวเลขจำนวนเต็ม")
