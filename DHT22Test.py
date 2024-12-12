import dht
from machine import Pin
from machine import UART
from time import sleep

sensor22 = dht.DHT22( Pin( 4 ))
sensor22.measure
def main():
    com = UART(1, 9600, tx=17, rx=16)
    com.init(9600)

#    while True:
#        choice = com.readline()

#        if choice == b'LED_ON\n':
#            led.value(0)
#           com.write(b'LED is ON!\n')  # 回應訊息給電腦端的Python
#        elif choice == b'LED_OFF\n':
#            led.value(1)
#            com.write(b'LED is OFF!\n')

if __name__ == '__main__':
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
#    main()