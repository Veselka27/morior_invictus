from machine import Pin, ADC, PWM
import utime

# define the pins used for the joystick
x_pin = Pin(26, Pin.IN)
y_pin = Pin(27, Pin.IN)
led = PWM(Pin(25))
led.freq(1000)
# create ADC objects to read the joystick inputs
x_adc = ADC(x_pin)
y_adc = ADC(y_pin)

# loop forever
while True:
    # read the joystick inputs
    x = x_adc.read_u16()
    y = y_adc.read_u16()
    led.duty_u16(x)
    # print the X and Y inputs
    print("X: {}, Y: {}".format(x, y))
    
    # wait for a short time to debounce the joystick inputs
    utime.sleep_ms(100)
