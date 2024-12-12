from machine import Pin

import time

r = Pin(23, Pin.OUT) #紅色
g = Pin(22, Pin.OUT) #綠色
b = Pin(21, Pin.OUT) #藍色


for i in range(10):
    g.value(0)          
    b.value(0)          
    r.value(1)          
    time.sleep(0.5) 

    b.value(0)          
    r.value(0) 
    g.value(1) 
    time.sleep(0.5)

    g.value(0)
    r.value(0)
    b.value(1)
    time.sleep(0.5)
g.value(0)
r.value(0)
b.value(0)