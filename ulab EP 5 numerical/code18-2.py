# code18-12
import ulab as np
import time
import esp32

def rndData(n):
    data = np.array([0]*n,dtype=np.float)
    for i in range(len(data)):
        data[i] = time.ticks_ms()/(esp32.raw_temperature()*esp32.hall_sensor())
    return data

data = rndData(128)
print("data ..... {}".format(data))
print("min ...... {} at {}".format(np.numerical.min(data),np.numerical.argmin(data)))
print("max ...... {} at {}".format(np.numerical.max(data),np.numerical.argmax(data)))
print("sum ...... {}".format(np.numerical.sum(data)))
print("average .. {}".format(np.numerical.mean(data)))
print("std ...... {}".format(np.numerical.std(data)))
