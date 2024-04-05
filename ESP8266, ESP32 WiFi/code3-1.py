#code3-1
import network as nw
ifSTA = nw.WLAN(nw.STA_IF)
print(ifSTA.active())
