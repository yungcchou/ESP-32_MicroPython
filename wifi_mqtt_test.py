import network, time, machine, ubinascii, dht
from machine import Pin
from umqtt.simple import MQTTClient

# ----------------------- MQTT broker parameters -------------------
broker_addr = "xxx.xxx.xxx.xxx"
broker_port = 1883
mqtt_user = "esp32"
mqtt_pw = "xxxxxxxxx"
client_id = ubinascii.hexlify(machine.unique_id())
topic = b'esp32/data/dht22'

# ----------------------- Wifi parameters -------------------
wifi_stations = [ {"SSID": "Jack-Office", "PASSWD": "xxxxxxxxxx" }]
station = network.WLAN(network.STA_IF)
station.active(False) # deactive wifi station
time.sleep(1)
station.active(True)  # inactive wifi station

# ------------------ finding wifi station (SSID) --------------
def find_ssid(target_ssid, target_pw):
    wifi_status = False
    networks = station.scan()
    for idx, net in enumerate(networks):
        ssid = net[0].decode('utf-8')
        bssid = net[1]
        print( f"{idx}-th ssid:{ssid}, bssid:{bssid}" )
        if ssid == target_ssid:
            print(f"SSID '{target_ssid}' is available.")
            print( f"Connect to {target_ssid} .", end="")
            station.connect(target_ssid, target_pw)
            for j in range( 30 ):
                if station.isconnected():
                    wifi_status = True
                    break
                else:
                    print( ".", end="" )
                    time.sleep( 1 )
        if wifi_status:
            break
    return wifi_status

if __name__ == "__main__":
    onBoard_LED = Pin( 2, Pin.OUT )
    select_station = 0
    if find_ssid(wifi_stations[select_station]["SSID"],
              wifi_stations[select_station]["PASSWD"]):
        print('\nConnection successful')
        for _ in range( 3 ):
            onBoard_LED.value(1)
            time.sleep(0.5)
            onBoard_LED.value(0)
            time.sleep(0.5)
        print(station.ifconfig())
        
        # -------- using DHT22 to measure temperature and humidity
        sensor22 = dht.DHT22( Pin( 4 ))
        sensor22.measure
        
        # -------- build MQTT Client -------------
        mqtt_client = MQTTClient( client_id, broker_addr, keepalive=60, user=mqtt_user, password=mqtt_pw)
        print( f'ESP32 --> {broker_addr} MQTT, subscribed to {topic} topic' )
        
        for i in range(10):
            sensor22.measure()
            temp22 = sensor22.temperature() # get DHT22's temperature data
            humi22 = sensor22.humidity()  # get DHT22's humidity data
            output_str = f'temperature(DHT22):{temp22}, Humidity(DHT22): {humi22}'
            print( output_str )
            
            mqtt_client.connect() # connect to broker
            mqtt_client.publish( topic, output_str.encode()) # publish data to MQTT broker
            
            for _ in range( 2 ):
                onBoard_LED.value(1)
                time.sleep(0.2)
                onBoard_LED.value(0)
                time.sleep(0.2)
            
            time.sleep(2)
    else:
        print( f"\nCan't connect to {wifi_stations[select_station]['SSID']}" )


