#import paho para usar MQTT 
#import mongoengine para guardar en DB
#import pandas para mapas de calor sobre imagen ?? valdría para análisis visual
import time
esp         = "['10:00:00:00:00:01' : {'RSSI' : -56},]"
espName     = "B/F/Z"
zone        = espName
mac_address = esp[2:19]
rssiStr     = esp[33:36]
rssi        = int(rssiStr)

rssiTrigger, distance = -57, rssi * -0.05 #Trigger must be a Physical Dipswitch in ESP32

print(mac_address,"is the nearest device and its RSSI LEVEL IS =", rssi, "dBs(","{0:.1f}".format(distance), "meters from BLE antenna )")
print("Hay {} dispositivos en la zona {}".format(esp.count("RSSI"),espName))

devicesCount = (esp.count("RSSI"))
presence = True if devicesCount >=1 else False


# ESTO DEBERÍA SER UN ARCHIVO CSV O DB EN LA NUBE (ACCESIBLE REMOTAMENTE)
worker_type = 'Mecánico' if mac_address == '10:00:00:00:00:01' else 'Other'
print(worker_type)

# DEEP SLEEP MODE CONTROLLER ? https://randomnerdtutorials.com/esp32-external-wake-up-deep-sleep/
tarea = True
print("ESP, SLEEP") if tarea==False else print("ESP, AWAKE")

while zone[0] == "B":
    if presence == True and tarea == True:
        if mac_address == "10:00:00:00:00:01" or worker_type == 'Mecánico':
            print("MQTT LED ON")
            time.sleep(1)
            print("MQTT LED OFF")
            time.sleep(1)
        else:
            break