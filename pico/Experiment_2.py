from machine import Pin

LED = Pin(25, Pin.OUT)
Button = Pin(0, Pin.IN, Pin.PULL_DOWN)

while True:
    LED.value(Button.value())


# Pin 0 > button > Pin 36