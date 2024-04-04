import ntptime
import machine
import socket
import network as nw

myESSID = "ชื่อAP"
myPassword = "รหัสผ่าน"
ifSTA = nw.WLAN(nw.STA_IF)
if (ifSTA.active() == False):
    rtc = machine.RTC()
    print(rtc.datetime())
    ifSTA.active(True)
    ifSTA.connect(myESSID, myPassword)
    while not ifSTA.isconnected():
        pass
    print("network configuration:\n{}".format(ifSTA.ifconfig()))
    ntptime.settime(timezone=7, erver = 'ntp.ntsc.ac.cn') # Bangkok +7
    ifSTA.active(False)
    print(rtc.datetime())
else:
    print("STA active Failed!")
