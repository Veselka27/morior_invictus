# Blinking LED

from machine import Pin
from time import sleep

LED = Pin(25, Pin.OUT)

while True:
    LED.toggle()
    sleep(0.5)
