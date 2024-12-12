import network

def connect_to_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        pass

    print('Connection successful')
    print('Network config:', station.ifconfig())
    
connect_to_wifi( "Jack-Office", "h304@1723" )
#connect_to_wifi( "Clear Sky", "0919570523" )
