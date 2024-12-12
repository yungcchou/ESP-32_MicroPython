from machine import Pin, PWM
import time

melody ={ 'Do': 523, 'Re': 587, 'Mi': 659,
          'Fa': 698, 'So': 784, 'La': 880,
          'Si': 988 }
buzzer = PWM(Pin(0, Pin.OUT))

buzzer.duty(100)
#buzzer.tone( 131, d=0.5)
buzzer.freq( 261 )
time.sleep( 1 )

#for key, val in melody.items():
#    buzzer.freq( melody[ key ] )
#    time.sleep(1)

#buzzer.duty(0)
#time.sleep(1)

#buzzer.duty(100)
#buzzer.freq(131)
#time.sleep(1)

#buzzer.duty(100)
#buzzer.freq(262)
#time.sleep(1)

buzzer.duty(0)
time.sleep(1)

print("buzzer done!")