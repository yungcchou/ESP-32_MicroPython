import network, time, machine, ubinascii, dht, json
from machine import Pin
from umqtt.simple import MQTTClient

broker_addr = "xxx.xxx.xxx.xxx"
broker_port = 1883
mqtt_user = "esp32"
mqtt_pw = "xxxxxxxx"
client_id = ubinascii.hexlify(machine.unique_id())

wifi_stations = [ {"SSID": "Jack-Office", "PASSWD": "xxxxxxxxx" }]
wifi_status = False
station = network.WLAN(network.STA_IF)
station.active(False)
time.sleep(1)

station.active(True)

def find_ssid(target_ssid, target_pw):
    global wifi_status
    networks = station.scan()
    i = 0
    for net in networks:
        ssid = net[0].decode('utf-8')
        bssid = net[1]
        print( f"{i}-th ssid:{ssid}, bssid:{bssid}" )
        i += 1
        if ssid == target_ssid:
            print(f"SSID '{target_ssid}' is available.")
            print( f"Connect to {target_ssid} .", end="")
            station.connect(target_ssid, target_pw)
            for j in range( 30 ):
                if station.isconnected():
                    print('Connection successful')
                    wifi_status = True
                    break
                else:
                    print( ".", end="" )
                    time.sleep( 1 )
            return True
    print(f"SSID '{target_ssid}' not found.")
    return False

onBoard_LED = Pin( 2, Pin.OUT )

select_station = 0
find_ssid(wifi_stations[select_station]["SSID"],
          wifi_stations[select_station]["PASSWD"])
if wifi_status:
    print('\nConnection successful')
    onBoard_LED.value(1)
    time.sleep(0.5)
    onBoard_LED.value(0)
    time.sleep(0.5)
    onBoard_LED.value(1)
    time.sleep(0.5)
    onBoard_LED.value(0)
    print(station.ifconfig())
    
    topic = b'esp32/data/dht22'
    mqtt_client = MQTTClient( client_id,
                              broker_addr,
                              keepalive=60,
                              user=mqtt_user,
                              password=mqtt_pw)
    
    
    sensor22 = dht.DHT22( Pin( 4 ))
    sensor22.measure
    print( f'Connected to {broker_addr} MQTT broker, subscribed to {topic} topic' )
    for i in range(70):
        sensor22.measure()
        temp22 = sensor22.temperature()
        humi22 = sensor22.humidity()
        output_str = json.dumps( {"temperature": temp22, "humidity": humi22} )
        
        print( output_str )
        
        mqtt_client.connect()
        mqtt_client.set_callback( output_str )
        mqtt_client.subscribe( topic )
        mqtt_client.publish( topic, output_str.encode())
        
        time.sleep(2)
else:
    print( f"\nCan't connect to {wifi_stations[select_station]['SSID']}" )



