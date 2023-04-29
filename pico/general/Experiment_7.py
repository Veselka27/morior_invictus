from machine import Pin, PWM
from time import sleep_ms, sleep
from _thread import start_new_thread

ButtonA = Pin(0, Pin.IN, Pin.PULL_DOWN)
ButtonB = Pin(1, Pin.IN, Pin.PULL_DOWN)

Red = Pin(10, Pin.OUT)
Yellow = Pin(11, Pin.OUT)
Green = Pin(12, Pin.OUT)
PedestrianRed = Pin(6, Pin.OUT)
PedestrianWait = Pin(7, Pin.OUT)
PedestrianGreen = Pin(8, Pin.OUT)

Buzzer = PWM(Pin(15))
Buzzer.duty_u16(0)
Frequency = 1000

CrossRequested = False

def red():
    Red.on()
    Yellow.off()
    Green.off()

def yellow():
    Red.off()
    Yellow.on()
    Green.off()

def green():
    Red.off()
    Yellow.off()
    Green.on()

def cycle_lights():
    red()
    sleep(5)
    yellow()
    sleep(1)
    green()
    sleep(5)
    yellow()
    sleep(1)
    
def PedestrianCross():
    global CrossRequested
    PedestrianRed.value(0)
    PedestrianGreen.value(1)
    PedestrianWait.value(0)
    OnTime = 50
    print("Beeping")
    for Beeping in range(10):
        Buzzer.duty_u16(32767)
        sleep_ms(OnTime)
        Buzzer.duty_u16(0)
        sleep_ms(1000-OnTime)
    print("End Beep Thread")
    PedestrianRed(1)
    PedestrianGreen(0)
    CrossRequested = False
    
def ButtonIRQHandler(pin):
    global CrossRequested
    if CrossRequested == False:
        print("Button Pressed")
        CrossRequested = True
        PedestrianWait.value(1)

ButtonA.irq(trigger=Pin.IRQ_RISING, handler=ButtonIRQHandler)
ButtonB.irq(trigger=Pin.IRQ_RISING, handler=ButtonIRQHandler)

Red.value(1)
Yellow.value(0)
Green.value(0)
PedestrianRed.value(1)
PedestrianGreen.value(0)
PedestrianWait.value(0)
sleep(2)

while True:
    if CrossRequested == True:
        start_new_thread(PedestrianCross, ())
        while PedestrianCross:
            sleep_ms(1)
    else:
        cycle_lights()