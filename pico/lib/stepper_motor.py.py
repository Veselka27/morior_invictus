from machine import Pin
import utime



# Define the motor steps sequence
STEPPER_SEQUENCE_ANTICLOCKWISE = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

STEPPER_SEQUENCE_CLOCKWISE = [
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0]
]


# Create Pin objects for stepper motor control pins
in1 = Pin(2, Pin.OUT)
in2 = Pin(3, Pin.OUT)
in3 = Pin(4, Pin.OUT)
in4 = Pin(5, Pin.OUT)

def set_stepper_pins(state):
    in1.value(state[0])
    in2.value(state[1])
    in3.value(state[2])
    in4.value(state[3])

def rotate_aclock(steps, delay_ms):
    for i in range(steps):
        for sequence in STEPPER_SEQUENCE_ANTICLOCKWISE:
            set_stepper_pins(sequence)
            utime.sleep_ms(delay_ms)

def rotate_clock(steps, delay_ms):
    for i in range(steps):
        for sequence in STEPPER_SEQUENCE_CLOCKWISE:
            set_stepper_pins(sequence)
            utime.sleep_ms(delay_ms)