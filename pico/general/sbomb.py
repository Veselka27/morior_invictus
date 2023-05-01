from machine import Pin, PWM
from utime import sleep

led_red = Pin(1, Pin.OUT)
led_green = Pin(2, Pin.OUT)
led_yellow = Pin(3, Pin.OUT)
buzzer = PWM(Pin(15))
time = 1
count = 0.1
freq = 2000
blinking = True

led_yellow.value(0)
led_red.value(0)
led_green.value(1)
sleep(2)
led_green.value(0)
led_yellow.value(1)
sleep(1)
led_yellow.value(0)

def beep():
    buzzer.freq(freq)  # Set a frequency of 1000 Hz for the buzzer
    buzzer.duty_u16(32768)  # Set a 50% duty cycle for the buzzer
    sleep(0.05)
    buzzer.duty_u16(0)  # Turn off the buzzer
    sleep(0.05)

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
        #break
    buzzer.duty_u16(32768)
    if blinking == False:
        led_red.value(1)
        led_green.value(1)
        led_yellow.value(1)
    print(time, freq)




