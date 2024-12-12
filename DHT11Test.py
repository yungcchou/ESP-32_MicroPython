import dht
from machine import Pin
from time import sleep

sensor11 = dht.DHT11( Pin( 4 ))

for i in range(10):
    sensor11.measure()
    temp11 = sensor11.temperature()
    humi11 = sensor11.humidity()
    
    print( 'temperature(DHT11):', temp11, 'Humidity(DHT11): ', humi11)
    sleep(2)

print( 'DHT demo done!! ' )