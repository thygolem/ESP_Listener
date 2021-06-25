#import paho para usar MQTT 
#import mongoengine para guardar en DB
#import pandas para mapas de calor sobre imagen ?? valdría para análisis visual
import time


esp = "{'10:00:00:00:00:01' : ['RSSIs' : -56] }"
mac_address = esp[2:19]
rssiStr = esp[33:36]
rssi = int(rssiStr)

rssiTrigger, distance = -55, rssi * -0.05 #estos valores cambian en f(x) de la zona que estemos, ya que BLE es sensible incluso a la humedad
# estos valores sería interesante 
devicesCount = (esp.count("RSSI"))

print(mac_address,"is the nearest device and its RSSI LEVEL IS =", rssi, "dBs(","{0:.1f}".format(distance), "meters from BLE antenna )")

print("¿AFORO MÁXIMO?")
aforo = int(input()) # molaría que este valor lo diera un dispositivo físico con un dipswitch (de 6 interruptores para usarlo en binario cuyo máximo son 4095 en decimnal).

if devicesCount >= aforo:
    print("El aforo máximo elegido es:", aforo, "\n")
    #MQTT PUBLISH devicesCount || MONGOENGINE WRITE TO JSON COLLECTION & JS-API EXPOSES
    if mac_address == "10:00:00:00:00:01" :
        if rssi >= rssiTrigger:
            print("""
                
                1) Operario\U0001f600        3) Herramienta\U0001F9F0
                2) Asistente\U0001F916       4) Otro
                ¿Qué necesitas? Elige número
                """)
            opcion = input()
            if (opcion == "1") or (opcion == "Operario"):
                print("Operario\U0001f600")
            elif (opcion == "2") or (opcion == "Asistente"):
                print("Asistente\U0001F916")
            elif (opcion == "3") or (opcion == "Herramienta") :
                print("Herramienta\U0001F9F0")
            elif (opcion == "4") or (opcion == "Otro"):
                time.sleep(0.5)
                print("  1 \U0001f600")
                time.sleep(0.5)
                print("   2 \U0001F916")
                time.sleep(0.5)
                print("     3 \U0001F9F0")
                time.sleep(0.5)
        else:
            print('Fuera de rango  . . . ')
            time.sleep(0.5)
            print('.')
            print('..')
            print('...')
            print('....')
            print('Esperando')

    else:
        print('NO HAY NÁ')
else:
    print("listening - - - - - - - - - - -")



#if __name__ == '__main__':
#    esp.main()
# Para automatizar en f(macType) (macType=x), habrá que hacer un JSON aparte donde especifique el tipo de activo, cada tipo de activo llevará un emoji de identificación




# Es interesante reconocer la MAC para contar cuántas hay presentes
# Usar el método find(mac_addresses_saved) para hacer lógicas en función de cada una


# [ pero la representación debe de ser en tº real en javacript web + phaespr
# [ estudiar la viabilidad de usar docker-compose.yml para ejecutar el entorno web y el script de python
# [ El stack sería Python=Backend, JS=Frontend. Sin embargo, quizás sea interesante realizar las lógicas de activación en JS y con WebSockets
