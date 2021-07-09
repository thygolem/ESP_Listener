import os
import json
import time
import datetime
# import paho.mqtt.client

#import mongoengine o PyMongo para guardar en DB
#import pandas para mapas de calor sobre imagen ?? valdría para análisis visual

import time
esp         = '{"timestamp":"2021-07-09T09:46:43Z","g_mac":"4C:11:AE:8B:4C:94","mac":"fd:04:ce:a4:90:e6","rssi":-94,"bleName":""}'
espName     = esp[45:62]
zone        = espName # ASIGNAR ALIAS EN DB
mac_address = esp[71:88]
rssi     = int(esp[97:100])

print(espName, mac_address, rssi)



