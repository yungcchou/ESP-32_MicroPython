from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

for i in range( 3 ):
    led.on()
    sleep(3)
    led.off()
    sleep(3)

print('LED repeat demo done!!' )