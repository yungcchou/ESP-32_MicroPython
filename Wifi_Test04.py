import network
import time

wifi_stations = [  {"SSID": "TP-Link_IoT_5G", "PASSWD": ""}]
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
            #station.connect(net[0], target_pw, bssid=bssid)
            #station.connect(net[0], auth=(WLAN.WPA2, target_pw))
            
            #station.connect(net[0], target_pw)
            #station.connect(net[0], bssid=bssid)
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

# Replace 'YourTargetSSID' with the SSID you're looking for
select_station = 1
find_ssid(wifi_stations[select_station]["SSID"],
          wifi_stations[select_station]["PASSWD"])
if wifi_status:
    print('\nConnection successful')
    print(station.ifconfig())
else:
    print( f"\nCan't connect to {wifi_stations[select_station]['SSID']}" )

