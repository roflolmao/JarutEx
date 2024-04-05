#code3-3
import network as nw
ifAP = nw.WLAN(nw.AP_IF)
if (ifAP.active() == True):
    print(ifAP.ifconfig())
