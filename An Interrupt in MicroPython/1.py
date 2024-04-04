import machine as mc
alertPin = mc.Pin(5, mc.Pin.IN) # D1

def alert_interrupt(pin):
    global interrupt_pin
    interrupt_pin = pin
    print("Alert!!!")

if __name__=="__main__":
    alertPin.irq(trigger=mc.Pin.IRQ_RISING, handler=alert_interrupt)
    while True:
        pass
