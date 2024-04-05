#code3-6
import network as nw
myESSID = "ชื่อAP"
myPassword = "รหัสผ่าน"
ifSTA = nw.WLAN(nw.STA_IF)
if (ifSTA.active() == False):
    ifSTA.active(True)
    ifSTA.connect(myESSID, myPassword)
    while not ifSTA.isconnected():
        pass
    print("network configuration:\n{}".format(ifSTA.ifconfig()))
ifSTA.active(False)
