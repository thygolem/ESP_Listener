#import paho para usar MQTT 
#import mongoengine para guardar en DB
#import pandas para mapas de calor sobre imagen ?? valdría para análisis visual
import time
esp         = '{"timestamp":"2021-07-09T09:46:43Z","g_mac":"4C:11:AE:8B:4C:94","mac":"10:00:00:00:00:01","rssi":-94,"bleName":""}'
espName     = esp[45:62]
espAlias    = "B/F/Z" # ASIGNAR ALIAS EN DB
nearMac     = esp[71:88]
rssi        = int(esp[97:100])
devicesCount = (esp.count("RSSI"))

print(espName, nearMac, rssi)


rssiTrigger, distance = -57, rssi * -0.05 #Trigger must be a Physical Dipswitch in ESP32

print(nearMac,"is the nearest device and its RSSI LEVEL IS =", rssi, "dBs(","{0:.1f}".format(distance), "meters from BLE antenna )")
print("Hay {} dispositivos en la zona {}".format(esp.count("RSSI"),espName))

devicesCount = (esp.count("RSSI"))
presence = True if devicesCount >=1 else False


# ESTO DEBERÍA SER UN ARCHIVO CSV O DB EN LA NUBE (ACCESIBLE REMOTAMENTE)
worker_type = 'Mecánico' if nearMac == '10:00:00:00:00:01' else 'Other'
print(worker_type)

# DEEP SLEEP MODE CONTROLLER ? https://randomnerdtutorials.com/esp32-external-wake-up-deep-sleep/
tarea = True
print("ESP, SLEEP") if tarea==False else print("ESP, AWAKE")

while espAlias[0] == "B":
    if presence == True and tarea == True:
        if nearMac == "10:00:00:00:00:01" or worker_type == 'Mecánico':
            print("MQTT LED ON")
            time.sleep(1)
            print("MQTT LED OFF")
            time.sleep(1)
        else:
            break