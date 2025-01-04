#libraries
import wifi
import serial
import websocket
from getmac import get_mac_address as gma
import os
import time
#from network import WLAN
#import websocket-client

#declare void functions
def func_wifi_login_to_access_point(): 

#websocket part
    ser = serial.Serial()
    ws = websocket.WebSocket()
    ws.connect("ws://echo.websocket.events/", origin="testing_websockets.com")
    ws.send("Hello, Server")
    print(ws.recv())

    #wlan = WLAN(mode=WLAN.STA)

    #path = 'ws://echo.websocket.events/'

#Serial.println part
    print("..... do_wifi_login_to_access_point() started .....")
    print("The MAC address for this board is: ")
    #print(wifi.macAddress())
    print(gma())

    #char part
    #ssid(config) = "geneseas"
    ssid = "geneseas"
    password = "geneseas"
    print("ssid is ", ssid)
    print("pw is ", password)

    #wlan.connect(ssid=ssid, auth=(WLAN.WPA2, password))
    #print("Connected to Wi-Fi. IP address:", wifi.ifconfig()[0])

    local_ip = "192.168.1.102"
    gateway = "192.168.1.1"
    subnet = "255.255.0.0"

    #ws.recv = 0

    #print()

    if ws.recv == 0:
        print("The MAC address for this board is: ")
        print(gma())
        #print("isWiFi_connected =", print(ws.status()))
    else:
        print("fail")

    ws.close()

def func_wifi_send_msg_to_mothership():
    print("...do_wifi_send_msg_to_mothership() started ...")
    print("**** UNDER CONSTRUCTION *****")
    #delay(1000)
    print(".... do_wifi_send_msg_to_mothership() completed ....\n")


if __name__ == "__main__":
    func_wifi_login_to_access_point()
    func_wifi_send_msg_to_mothership()

#ser = serial.Serial('202')
#print(ser.name)