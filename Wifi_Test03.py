import network
import time

#ssid = 'Jack-Office'
#password = 'h304@1723'

ssid = 'Clear Sky'
password = '0919570523'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

timeout = 10  # seconds
start_time = time.time()

while not station.isconnected():
    if time.time() - start_time > timeout:
        print("Connection timed out.")
        break
    pass

if station.isconnected():
    print('Connection successful')
    print(station.ifconfig())
else:
    print('Failed to connect')