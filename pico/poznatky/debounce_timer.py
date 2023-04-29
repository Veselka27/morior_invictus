from machine import Pin, Timer

Button = Pin(0, Pin.IN, Pin.PULL_DOWN)
LED = Pin(25, Pin.OUT)
LEDstate = False
debounce_timer = Timer()

def ButtonIRQHandler(pin):
    global LEDstate
    debounce_timer.init(mode=Timer.ONE_SHOT, period=50, callback=debounce_callback)
    # start the timer with a 50ms debounce time

def debounce_callback(timer):
    global LEDstate
    if Button.value() == 1:  # check if the button is still pressed after debounce time
        LEDstate = not LEDstate

Button.irq(trigger=Pin.IRQ_RISING, handler=ButtonIRQHandler)

while True:
    LED.value(LEDstate)
