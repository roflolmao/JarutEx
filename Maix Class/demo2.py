# Untitled - By: cid - Thu Sep 9 2021

import gc
import os
import sys
import machine as mc
import time as tm
import image, time, lcd

lcd.init(freq=15000000)
gc.enable()
gc.collect()

clock = time.clock()
#mc.freq(400000000)

def isPrime(x):
    i = 2
    while (i < x):
        if x%i == 0:
            return False
        i = i+1
    if (i == x):
        return True
    return False

def testPrimeNumber(maxN):
    counter = 0
    t0 = tm.ticks_ms()
    for n in range(2, maxN):
        if isPrime(n):
            counter+=1
    t1 = tm.ticks_ms()
    print("Found {} in {} msecs.".format(counter,abs(t1-t0)))

testPrimeNumber(2000)
