#import paho para usar MQTT 
#import mongoengine para guardar en DB
#import pandas para mapas de calor sobre imagen ?? valdría para análisis visual

b = False
s3 = "{'10:00:00:00:00:01' : ['RSSI' : -56] }"
mac_address = s3[2:19]
rssiStr = s3[33:36]
rssi = int(rssiStr)

rssiTrigger, distance = -57, rssi * -0.05 #estos valores cambian en f(x) de la zona que estemos, ya que BLE es sensible incluso a la humedad

devicesCount = (s3.count("RSSI"))

print(mac_address,"is the nearest device and its RSSI LEVEL IS =", rssi, "dBs(","{0:.1f}".format(distance), "meters from BLE antenna )")


print("¿AFORO MÁXIMO?")
aforo = int(input()) # molaría que este valor lo diera un dispositivo físico con un dipswitch, sin necesidad de LCD  


if devicesCount >= aforo:
    print("El aforo máximo elegido es", aforo, ", ¡ ACTIVANDO EQUIPOS DE SONIDO !")
    #MQTT PUBLISH devicesCount || MONGOENGINE WRITE TO JSON COLLECTION & JS-API EXPOSES
    if mac_address == "10:00:00:00:00:01" :
        if rssi >= rssiTrigger:
            print(" device 1")
            print(" device 2")
            print(" device 3")
            print("\U0001F480 BEGIN PHASER ERA \U0001F480")




    else:
        print('NO HAY NÁ')
else:
    print("listening - - - - - - - - - - -")

# Para automatizar en f(macType) (macType=x), habrá que hacer un JSON aparte donde especifique el tipo de activo, cada tipo de activo llevará un emoji de identificación




# Es interesante reconocer la MAC para contar cuántas hay presentes
# Usar el método find(mac_addresses_saved) para hacer lógicas en función de cada una


# [ pero la representación debe de ser en tº real en javacript web + phas3r
# [ estudiar la viabilidad de usar docker-compose.yml para ejecutar el entorno web y el script de python
# [ El stack sería Python=Backend, JS=Frontend. Sin embargo, quizás sea interesante realizar las lógicas de activación en JS y con WebSockets


