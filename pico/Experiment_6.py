# Red,Yellow and Green LED blinking and a beeping Buzzer controled by Button

from machine import Pin, PWM
import utime
import _thread

Button = Pin(0, Pin.IN, Pin.PULL_DOWN)
Red = Pin(10, Pin.OUT)
Yellow = Pin(11, Pin.OUT)
Green = Pin(12, Pin.OUT)

Buzzer = PWM(Pin(15))
Buzzer.duty_u16(0)
Frequency = 1000

Beeping = False

def Beep():
    global Beeping
    OnTime = 50
    print("Start Beeping Thread")
    while Beeping:
        Buzzer.duty_u16(32767)
        utime.sleep_ms(OnTime)
        Buzzer.duty_u16(0)
        utime.sleep_ms(1000 - OnTime)
    print("End Beeping Thread")

def ButtonIRQHandler(button):
    global Beeping
    if Beeping == False:
        print("Start Beep")
        Beeping = True
        _thread.start_new_thread(Beep, ())
    else:
        Beeping = False
        print("Stop Beep")

Button.irq(trigger = Pin.IRQ_RISING, handler = ButtonIRQHandler)

Red.value(0)
Yellow.value(0)
Green.value(0)
while True:
    Red.toggle()
    utime.sleep_ms(100)
    Yellow.toggle()
    utime.sleep_ms(100)
    Green.toggle()
    utime.sleep_ms(100)
# Pin 0(1) > Button > 36
# Pin 15(20) > Buzzer > 38
# Pin 10(14) > Red > 330 R > 38
# Pin 11(15) > Yellow > 330 R > 38
# Pin 12(16) > Green > 330 R > 38