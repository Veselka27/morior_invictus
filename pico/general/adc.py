from machine import ADC, PWM, Pin
from utime import sleep_ms

green = PWM(Pin(0))
red = PWM(Pin(1))
yellow = Pin(2, Pin.OUT)
x_pin = ADC(26)
y_pin = ADC(27)
button = Pin(3, Pin.IN, Pin.PULL_UP)

while True:
    x = x_pin.read_u16()
    y = y_pin.read_u16()
    x = x - 1
    y = y - 1
    green.duty_u16(x)
    red.duty_u16(y)
    yellow.value(not button.value())
    print(f"X: {x} Y: {y}")
    sleep_ms(100)