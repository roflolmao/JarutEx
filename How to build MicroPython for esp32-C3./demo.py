import gc
import time as tm
import machine as mc

gc.enable()
gc.collect()

mc.freq(160000000)

def is_prime(x):
    i = 2
    while (i < x):
        if x%i == 0:
            return False
        i = i+1
    if (i == x):
        return True
    return False

def test_prime_number(maxN):
    counter = 0
    t0 = tm.ticks_ms()
    for n in range(2, maxN):
        if is_prime(n):
            counter+=1
    t1 = tm.ticks_ms()
    print("Found {} in {} msecs.".format(counter,abs(t1-t0)))
    
test_prime_number(2000)
