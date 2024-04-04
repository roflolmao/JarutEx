#code26-1
from time import time
from time import monotonic
from time import sleep
import RPi.GPIO as GPIO

pinM1a = 17
pinM1b = 18
pinM2a = 22
pinM2b = 23


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinM1a, GPIO.OUT)
    GPIO.setup(pinM1b, GPIO.OUT)
    GPIO.setup(pinM2a, GPIO.OUT)
    GPIO.setup(pinM2b, GPIO.OUT)

def deinit():
    GPIO.cleanup()
    
def stop():
    GPIO.output(pinM1a, False)
    GPIO.output(pinM1b, False)
    GPIO.output(pinM2a, False)
    GPIO.output(pinM2b, False)

def forward():
    GPIO.output(pinM1a, True)
    GPIO.output(pinM1b, False)
    GPIO.output(pinM2a, False)
    GPIO.output(pinM2b, True)

def left():
    GPIO.output(pinM1a, True)
    GPIO.output(pinM1b, False)
    GPIO.output(pinM2a, True)
    GPIO.output(pinM2b, False)

def right():
    GPIO.output(pinM1a, False)
    GPIO.output(pinM1b, True)
    GPIO.output(pinM2a, False)
    GPIO.output(pinM2b, True)

def backward():
    GPIO.output(pinM1a, False)
    GPIO.output(pinM1b, True)
    GPIO.output(pinM2a, True)
    GPIO.output(pinM2b, False)

init()
forward()
sleep(0.5)
stop()
sleep(1)
backward()
sleep(0.5)
stop()
sleep(1)
left()
sleep(0.5)
stop()
sleep(1)
right()
sleep(0.5)
stop()
sleep(1)
deinit()
