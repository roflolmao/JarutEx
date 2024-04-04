import network as nw
import ntptime
from machine import RTC
import time
print("Before : {}".format(time.localtime()))
myESSID = "ชื่อAP"
myPassword = "รหัสผ่านของAP"
ifSTA = nw.WLAN(nw.STA_IF)
if (ifSTA.active() == False):
    ifSTA.active(True)
    ifSTA.connect(myESSID, myPassword)
    while not ifSTA.isconnected():
        pass
    print("network configuration:\n{}".format(ifSTA.ifconfig()))
    rtc = RTC()
    ntptime.settime()
    print("After : {}".format(time.localtime()))
ifSTA.active(False)
