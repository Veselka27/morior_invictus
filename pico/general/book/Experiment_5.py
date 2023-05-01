# LED and Red LED with two Buttons controling each and Interrupt ReQuest

from machine import Pin
 
LED = Pin(25, Pin.OUT)
Red = Pin(10, Pin.OUT)

ButtonA = Pin(0, Pin.IN, Pin.PULL_DOWN)
ButtonB = Pin(1, Pin.IN, Pin.PULL_DOWN)

LEDState = False
RedState = False

def ButtonAIRQHandler(pin):
    global LEDState
    if pin == ButtonA:
        if LEDState == True:
                LEDState = False
        else:
            LEDState = True

def ButtonBIRQHandler(pin):
    global RedState
    if pin == ButtonB:
        if RedState == True:
                RedState = False
        else:
            RedState = True

ButtonA.irq(trigger = Pin.IRQ_RISING, handler = ButtonAIRQHandler)
ButtonB.irq(trigger = Pin.IRQ_RISING, handler = ButtonBIRQHandler)

while True:
    LED.value(LEDState)
    Red.value(RedState)

# Pin 0(1) > ButtonA > Pin (36)
# Pin 1(2) > ButtonB > Pin (36)
# Pin 10(14) > Red > 330 R > PIN (38)