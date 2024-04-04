# code19-2
import machine
u2=machine.UART(2, baudrate=9600, rx=22, tx=21, timeout=10)
print(u2)
while True:
    data = u2.readline()
    if (data != None):
        if (b'$GPRMC' in data):
            s = data.decode() # convert bytearray to string
            info = s.split(',')
            print("Time(UTC) hhmmss.ms: {}".format(info[1]))
            if (info[2] == 'V'):
                print("Navigation receiver warning")
            else:
                print("Lat:{},{} Lon:{},{}".format(info[3],info[4],info[5],info[6]))
                if (len(info[7])>0):
                    print("Speed over ground {} knots".format(info[7]))
                print("Track made good, degrees true {}".format(info[8]))
                print("Magnetic Veriation {} degree(s)".format(info[10]))
                print("E/W: {}".format(info[11]))
            print("Date (ddmmyy): {}".format(info[9]))
            print("------------")
