# Red,Yellow and Green LED blinking and a beeping Buzzer controled by Button

from machine import Pin, PWM, Timer
from utime import sleep_ms
from _thread import start_new_thread
debounce_timer = Timer()

Button = Pin(0, Pin.IN, Pin.PULL_DOWN)
Red = Pin(13, Pin.OUT)
Yellow = Pin(14, Pin.OUT)
Green = Pin(15, Pin.OUT)

Buzzer = PWM(Pin(16))
Buzzer.duty_u16(0)
Frequency = 1000

Beeping = False

def Beep():
    global Beeping
    OnTime = 50
    print("Start Beeping Thread")
    while Beeping:
        Buzzer.duty_u16(32767)
        sleep_ms(OnTime)
        Buzzer.duty_u16(0)
        sleep_ms(1000 - OnTime)
    print("End Beeping Thread")

def ButtonIRQHandler(pin):
    global Beeping
    debounce_timer.init(mode = Timer.ONE_SHOT, period = 50, callback = debounce_callback)

def debounce_callback(timer):
    global Beeping
    if Button.value() == 1:
        if Beeping == False:
            print("Start Beep")
            Beeping = True
            start_new_thread(Beep, ())
        else:
            Beeping = False
            print("Stop Beep")

Button.irq(trigger = Pin.IRQ_RISING, handler = ButtonIRQHandler)

Red.value(0)
Yellow.value(0)
Green.value(0)
while True:
    Red.toggle()
    sleep_ms(100)
    Yellow.toggle()
    sleep_ms(100)
    Green.toggle()
    sleep_ms(100)
# Pin 0(1) > Button > 36
# Pin 15(20) > Buzzer > 38
# Pin 10(14) > Red > 330 R > 38
# Pin 11(15) > Yellow > 330 R > 38
# Pin 12(16) > Green > 330 R > 38