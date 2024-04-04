# demoRandomEsp32
import random

print("random.random() ...............: {}".format(random.random()))
print("random.uniform(5,10) ..........: {}".format(random.uniform(5,10)))
print("random.randint(5,10) ..........: {}".format(random.randint(5,10)))
print("random.randrange(5, 20, 4) ....: {}".format(random.randrange(5, 20, 4)))

mcu = ("mcs51","pic","avr","stm32","esp8266","esp32")
print("random.choice(mcu) ............: {}".format(random.choice(mcu)))
