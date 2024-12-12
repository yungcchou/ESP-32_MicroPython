import dht
from machine import Pin
from machine import UART
from time import sleep

sensor22 = dht.DHT22( Pin( 4 ))
sensor22.measure

com = UART(1, 9600, tx=17, rx=16)
com.init(9600)
for i in range(10):
    sensor22.measure()
    temp22 = sensor22.temperature()
    humi22 = sensor22.humidity()
    print( 'temperature(DHT22):', temp22, 'Humidity(DHT22): ', humi22)
    com.write(b'temperature(DHT22):{temp22}\n')
    sleep(2)

print( 'DHT demo done!! ' )
