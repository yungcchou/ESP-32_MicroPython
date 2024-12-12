from machine import Pin, PWM
import time

# beeper = PWM( Pin( 2, Pin.OUT))
beeper = PWM(Pin(2), freq=5000, duty_u16=32768)
notes = [ 333, 445, 0, 56, 899, 4444]
beeper.duty( 0 )
beeper.duty( 512 )
beeper.freq( 445 )
time.sleep(1)
beeper.duty( 0 )

for note in notes:
    if note == 0:
        beeper.duty( 0 )
    else:
        beeper.duty( 512 )
        beeper.freq( note )
    time.sleep(1)
    beeper.duty(0)
    time.sleep(0.1)
beeper.duty(0)
beeper.duty(0)
beeper.duty(0)
beeper.freq( 40 )
print("beep done!")