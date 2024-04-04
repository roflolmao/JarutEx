#code6-2.py
# (C) 2020, JarutEx
import os
import time
from machine import SDCard
if (not('sd' in os.listdir())):
    sd = SDCard()
    os.mount(sd,'/sd')
print(os.listdir('/'))
print(os.listdir('/sd'))
if ('log.txt' in os.listdir('/sd')):
    log = open('/sd/log.txt','a')
else:
    log = open('/sd/log.txt','w')
lcTime = time.localtime()
log.write("date {}/{}/{} , time {}:{}:{}\n".format( lcTime[0], lcTime[1], lcTime[2], lcTime[4], lcTime[5], lcTime[6]))
log.close()
log = open('/sd/log.txt','r')
dLog = log.read()
log.close()
print("data from log.txt\n{}".format(dLog))
