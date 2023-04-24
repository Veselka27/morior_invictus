from machine import Pin
from utime import sleep

button_red = Pin(15, Pin.IN, Pin.PULL_DOWN	)
button_black = Pin(2, Pin.IN, Pin.PULL_UP)

while True:
    if button_red.value() == 1:
        print("red")
    if button_black.value() == 0:
        print("black")
    
    sleep(0.25)