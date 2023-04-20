from machine import Pin
from utime import sleep_ms

Red1 = Pin(0, Pin.OUT)
Yellow1 = Pin(1,Pin.OUT)
Green1 = Pin(2, Pin.OUT)
Red2 = Pin(3, Pin.OUT)
Yellow2 = Pin(4, Pin.OUT)
Green2 = Pin(5, Pin.OUT)
Button = Pin(6, Pin.IN, Pin.PULL_DOWN)
Direction = False

def ButtonIRQHandler(pin):
	global Direction
	if Direction == True:
		Red1.value(0)
		Yellow1.value(0)
		Green1.value(0)
		Red2.value(0)
		Yellow2.value(0)
		Green2.value(0)
		Direction = False
	else:
		Red1.value(0)
		Yellow1.value(0)
		Green1.value(0)
		Red2.value(0)
		Yellow2.value(0)
		Green2.value(0)
		Direction = True

Button.irq(trigger = Pin.IRQ_RISING, handler = ButtonIRQHandler)

Red1.value(0)
Yellow1.value(0)
Green1.value(0)
Red2.value(0)
Yellow2.value(0)
Green2.value(0)

while True:
	if Direction == True:
		Red1.toggle()
		sleep_ms(80)
		Yellow1.toggle()
		sleep_ms(80)
		Green1.toggle()
		sleep_ms(80)
		Red2.toggle()
		sleep_ms(80)
		Yellow2.toggle()
		sleep_ms(80)
		Green2.toggle()
		sleep_ms(80)
	else:
		Red1.toggle()
		sleep_ms(80)
		Green2.toggle()
		sleep_ms(80)
		Yellow2.toggle()
		sleep_ms(80)
		Red2.toggle()
		sleep_ms(80)
		Green1.toggle()
		sleep_ms(80)
		Yellow1.toggle()
		sleep_ms(80)