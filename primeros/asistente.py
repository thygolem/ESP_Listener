#import paho para usar MQTT 
#import mongoengine para guardar en DB
#import pandas para mapas de calor sobre imagen ?? valdría para análisis visual
import time
esp         = "['10:00:00:00:00:01' : {'RSSI' : -56},]"
espName     = "B/F/Z"
mac_address = esp[2:19]
rssiStr     = esp[33:36]
rssi        = int(rssiStr)

rssiTrigger, distance = -57, rssi * -0.05 #Trigger must be a Physical Dipswitch in ESP32

print(mac_address,"is the nearest device and its RSSI LEVEL IS =", rssi, "dBs(","{0:.1f}".format(distance), "meters from BLE antenna )")
print("Hay {} dispositivos en la zona {}".format(esp.count("RSSI"),espName))

devicesCount = (esp.count("RSSI"))
presence = True if devicesCount >=1 else False

# ESTO DEBERÍA SER UN ARCHIVO CSV O DB EN LA NUBE (ACCESIBLE REMOTAMENTE)
worker_type = 'Mecánico' if mac_address == '10:00:00:00:00:01'else 'Other'
print(worker_type)

# DEEP SLEEP MODE CONTROLLER ?
tarea = True
print("MQTT publish OFF") if tarea==False else print("MQTT PUBLISH ON")


if (presence == True and tarea == True):
    print(" Comprobando en DB qué tareas hay para este tipo de operario en esta zona  \n")
    time.sleep(2.5)
    #MQTT PUBLISH devicesCount || MONGOENGINE WRITE TO JSON COLLECTION & JS-API EXPOSES
    if worker_type == "Mecánico" :
            print("mandando documentación de esta tarea en esta zona a grupo de telegram asignado al tipo de operario que está en esta zona")
    else:
        print('Esta tarea no pertenece a este operario')
else:
    print("still listening - - - - - - - - - - -")
    time.sleep(0.5)
    print("-")
    print("- -")
    print("- - -")
    print("- - - - ")


# recepción de 
if help == True:
    print("Inicializando asistente, comunicando por telegram")
    time.sleep(2.5)
    print("""           
                                ¿Qué necesitas?
                1) Operario\U0001f600        3) Herramienta\U0001F9F0
                2) Asistente\U0001F916       4) Otro
                                 Elige número
                """)
    opcion = input()
    if (opcion == "1" or opcion == "Operario"):
        print("Operario\U0001f600")
    elif (opcion == "2" or opcion == "Asistente"):
        print("Asistente\U0001F916")
    elif (opcion == "3" or opcion == "Herramienta") :
        print("Herramienta\U0001F9F0")
    elif (opcion == "4" or opcion == "Otro"):
        time.sleep(0.5)
        print("  1 \U0001f600")
        time.sleep(0.5)
        print("   2 \U0001F916")
        time.sleep(0.5)
        print("     3 \U0001F9F0")
        time.sleep(0.5)