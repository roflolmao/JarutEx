#code25-1
from time import time
from time import monotonic
from time import sleep
import RPi.GPIO as GPIO

pinTrig = 20
pinEcho = 21
mps = 343 # Metre per second (Sound speed)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinTrig, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

GPIO.output(pinTrig, False)
sleep(0.5)
GPIO.output(pinTrig, True)
sleep(0.00001)
GPIO.output(pinTrig, False)

# send trig
GPIO.output(pinTrig, True)
sleep(0.00001)
GPIO.output(pinTrig, False)
# start count
t0 = monotonic()
while GPIO.input(pinEcho) == 0:
    # wait for echo
    pass
while GPIO.input(pinEcho) == 1:
    # wait for end echo
    pass
t1 = monotonic()
echoTime = t1-t0
distance = (echoTime*mps*100)/2
print("{} cm.".format(distance))
GPIO.cleanup()
