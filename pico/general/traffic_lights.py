from machine import Pin
import time

red_led = Pin(13, Pin.OUT)
yellow_led = Pin(14, Pin.OUT)
green_led = Pin(15, Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_DOWN)

def red():
    red_led.on()
    yellow_led.off()
    green_led.off()

def yellow():
    red_led.off()
    yellow_led.on()
    green_led.off()

def green():
    red_led.off()
    yellow_led.off()
    green_led.on()

def cycle_lights():
    red()
    time.sleep(5)
    yellow()
    time.sleep(1)
    green()
    time.sleep(5)
    yellow()
    time.sleep(1)

def button_pressed(pin):
    global state
    if state == 'off':
        state = 'red'
        red()
    elif state == 'red':
        state = 'yellow'
        yellow()
    elif state == 'yellow':
        state = 'green'
        green()
    elif state == 'green':
        state = 'off'
        red_led.off()
        yellow_led.off()
        green_led.off()

button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)
state = 'off'

while True:
    if state != 'off':
        cycle_lights()
