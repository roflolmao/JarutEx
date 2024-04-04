#code19-1
import machine
u2=machine.UART(2, baudrate=9600, rx=22, tx=21, timeout=10)
print(u2)
while True:
    data = u2.readline()
    if (data != None):
        print(data)
