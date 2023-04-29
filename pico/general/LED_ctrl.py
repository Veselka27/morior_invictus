# LED on, off

from machine import Pin

LED = Pin(25, Pin.OUT)
LED.toggle()