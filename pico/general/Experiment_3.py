# Button and LED with Interrupt ReQuest

from machine import Pin

LED = Pin(25, Pin.OUT)
Button = Pin(0, Pin.IN, Pin.PULL_DOWN)
LEDstate = False

def ButtonIRQHandler(pin):
    global LEDstate
    if LEDstate == True:
        LEDstate = False
    else:
        LEDstate = True

Button.irq(trigger = Pin.IRQ_RISING, handler = ButtonIRQHandler)

while True:
    LED.value(LEDstate)

# Pin 0 > button > Pin 36