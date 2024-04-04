# code18-16 : poly
import ulab as np
import esp32
import time

# 2*3^2+4*3^1+2*3^0 = ?
p = np.array([2,4,2])
a = np.array([3])
print('value of p(a): ', np.poly.polyval(p, a))

# 2*3^4+3*3^3+1*3^2+2*3^1+0*3^0 = ?
# 2*2^4+3*2^3+1*2^2+2*2^1+0*2^0 = ?
p = np.array([2,3,1,2,0])
a = np.array([3,2])
print('value of p(a): ',np.poly.polyval(p, a))

x = np.linspace(0,10,15)
y = np.array([0]*15,dtype=np.float)
for idx in range(15):
    y[idx] = (x[idx]*x[idx])/2.0+(esp32.hall_sensor()*(time.ticks_ms()/1000000.0))
print(x)
print(y)
print(np.poly.polyfit(x,y,2))
print(np.poly.polyfit(y,2))
