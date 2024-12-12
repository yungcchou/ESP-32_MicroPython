import network

def scan_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    networks = wlan.scan()
    for ssid, bssid, channel, RSSI, authmode, hidden in networks:
        print(f"SSID: [{ssid.decode('utf-8')}], Channel:  {channel}, RSSI: {RSSI}, BSSID: {bssid}")


scan_wifi()

