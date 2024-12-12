from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

led.on()
sleep(3)
led.off()