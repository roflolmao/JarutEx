import serial
s = serial.Serial()
portNames = [
    "/dev/ttyUSB0",
    "/dev/ttyUSB1",
    "/dev/ttyUSB2",
    "/dev/ttyUSB3",
    "/dev/ttyACM0",
    "/dev/ttyACM1",
    "/dev/ttyACM2",
    "/dev/ttyACM3"
]
for pname in portNames:
    try:
        s.port = pname
        s.open()
        if s.isOpen():
            print("Found {}.".format(pname))
    except:
        pass
print("End of program.")
