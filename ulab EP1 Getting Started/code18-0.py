# code18-0 : Benchmark
import time
import ulab as np
import sys

print(sys.platform)

a = [0.0]*1000
b = range(1000)
print('python:')
t0 = time.ticks_us()
[a[i]+b[i] for i in range(1000)]
print("execution time for add = {} us".format(time.ticks_us()-t0))
t0 = time.ticks_us()
[a[i]*b[i] for i in range(1000)]
print("execution time for multiply = {} us".format(time.ticks_us()-t0))

a = np.linspace(0, 10, num=1000)
b = np.ones(1000)
print('ulab:')
t0 = time.ticks_us()
a+b
print("execution time for add = {} us".format(time.ticks_us()-t0))
t0 = time.ticks_us()
a*b
print("execution time for multiply = {} us".format(time.ticks_us()-t0))
