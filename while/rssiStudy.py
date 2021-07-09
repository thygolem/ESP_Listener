#import paho para usar MQTT 
#import mongoengine para guardar en DB
#import pandas para mapas de calor sobre imagen ?? valdría para análisis visual
import time

esp         = "['10:00:00:00:00:01' : {'RSSI' : -10 },]"
espName     = "B/F/Z"
zone        = espName
mac_address = esp[2:19]
rssiStr     = esp[33:36]
rssi        = int(rssiStr)

uno = 1
idx = 1

    
