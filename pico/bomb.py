from machine import Pin, PWM
from utime import sleep

led_red = Pin(1, Pin.OUT)
led_green = Pin(2, Pin.OUT)
led_yellow = Pin(3, Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_DOWN)
buzzer = PWM(Pin(15))

led_yellow.value(0)
led_red.value(0)
time = 1
count = 0.1
freq = 2000
blinking = False
green = True

def button_handler(pin):
    if button.value() == 1:
        pressed()
    else:
        released()

def pressed():
    print("button is pressed")
    led_yellow.value(1)
    led_green.value(0)
    while button.value() == 1:  # wait for the button to be released
        pass
    led_green.value(0)

def released():
    print("button is released")
    global time, count, blinking, freq
    led_green.value(0)
    led_yellow.value(0)
    blinking = True
    while blinking:
        led_red.value(1)
        beep()
        freq += 50
        sleep(time)
        led_red.value(0)
        sleep(time)
        time -= count
        if time <= 0.3:
            count = 0.01
        elif time <= 0.1:
            count = 0.005
        if time <= 0:
            blinking = False
        print(time, freq)

def beep():
    buzzer.freq(freq)  # Set a frequency of 1000 Hz for the buzzer
    buzzer.duty_u16(32768)  # Set a 50% duty cycle for the buzzer
    sleep(0.05)
    buzzer.duty_u16(0)  # Turn off the buzzer
    sleep(0.05)

button.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button_handler)

while True:
    led_green.value(int(green))
    green = not green
