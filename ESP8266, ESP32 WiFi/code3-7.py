#code3-7
import network as nw
ifSTA = nw.WLAN(nw.STA_IF)
if (ifSTA.active() == False):
    ifSTA.active(True)
    listAPs = ifSTA.scan()
    for AP in listAPs:
        print("{}".format(AP[0]))
ifSTA.active(False)
