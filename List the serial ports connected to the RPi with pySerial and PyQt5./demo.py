# -*- coding: UTF-8 -*-
import sys
import glob
import serial

ports = glob.glob('/dev/tty[A-Za-z]*')
result = []
for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        result.append(port)
    except (OSError, serial.SerialException):
        pass
if (len(result) == 0):
    print("ไม่พบพอร์ตอนุกรม")
else:
    print("พบพอร์ตอนุกรมดังรายการต่อไปนี้:")
    for p in result:
        print("{}".format(p))
