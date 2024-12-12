from machine import Pin, PWM
import time

buzzer = PWM(Pin(2, Pin.OUT), freq=440, duty=56)

CL = [0, 131, 147, 165, 175, 196, 211, 248]
CM = [0, 262, 294, 330, 350, 393, 441, 495]
CH = [0, 525, 589, 661, 700, 786, 882, 990]

song = [CM[5], CM[5], CM[6], CH[1], CM[6], CM[5], CM[3], CM[2], CM[5], CM[6], CH[1], CH[1], CM[6], CH[1], CH[2], CH[3], CH[2],
        CH[1], CH[2], CH[3], CH[5], CH[3], CH[2], CH[3], CH[1], CH[3], CH[2], CH[2], CH[1], CM[6], CM[5], CM[6], CM[5], CM[3],
        CM[2], CM[3], CM[2], CM[3], CM[5], CM[5], CM[6], CM[5], CM[2], CH[3], CH[1], CH[2], CM[6], CM[5], CM[3], CM[5], CM[3],CM[2], CM[3],
        CH[3], CH[3], CH[2], CH[1], CH[2], CH[3], CH[5], CH[2], CH[2], CH[3], CM[7], CM[6], CM[7], CM[6], CM[7], CM[5], CM[6], CH[1]]

beat = [2, 4, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 4,
        1, 1, 4, 1, 1, 1, 1, 4, 2, 2, 1, 1, 1, 1, 2, 4, 2,
        1, 1, 4, 2, 2, 4, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4,
        2, 1, 1, 1, 1, 1, 1, 2, 4, 1, 1, 1, 1, 1, 2, 1, 8, 1]
for i in range(len(song)):
    buzzer.freq(song[i])
    time.sleep(beat[i] * 0.2)

buzzer.deinit()
print("beep done!")
