# special blink when plugged in

from machine import Pin
from time import sleep

LED = Pin(25, Pin.OUT)

LED.toggle()
sleep(1)
LED.value(1)
sleep(1)
LED.value(0)
sleep(0.2)
LED.value(1)
sleep(0.2)
LED.value(0)
sleep(0.1)
LED.value(1)
sleep(0.1)
LED.value(0)
