from machine import Pin
 
LED1 = Pin(25, Pin.OUT)
LED2 = Pin(10, Pin.OUT)

ButtonA = Pin(0, Pin.IN, Pin.PULL_DOWN)
ButtonB = Pin(1, Pin.IN, Pin.PULL_DOWN)

LEDState1 = False
LEDState2 = False

def ButtonAIRQHandler(pin):
    global LEDState1
    if LEDState1 == True:
            LEDState1 = False
    else:
        LEDState1 = True

def ButtonBIRQHandler(pin):
    global LEDState2
    if LEDState2 == True:
            LEDState2 = False
    else:
        LEDState2 = True

ButtonA.irq(trigger = Pin.IRQ_RISING, handler = ButtonAIRQHandler)
ButtonB.irq(trigger = Pin.IRQ_RISING, handler = ButtonBIRQHandler)

while True:
    LED1.value(LEDState1)
    LED2.value(LEDState2)

# Pin 0(1) > ButtonA > Pin (36)
# Pin 1(2) > ButtonB > Pin (36)
# Pin 10(14) > LED1 > 330 R > PIN (38)