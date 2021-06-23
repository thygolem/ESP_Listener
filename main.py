#import paho para usar MQTT 
#import mongoengine para guardar en DB
#import pandas para mapas de calor sobre imagen ?? valdría para análisis,

# [ pero la representación debe de ser en tº real en javacript web + phas3r
# [ estudiar la viabilidad de usar docker-compose.yml para ejecutar el entorno web y el script de python
# [ El stack sería Python=Backend, JS=Frontend. Sin embargo, quizás sea interesante realizar las lógicas de activación en JS y con WebSockets

a = 0
b = None
s3 = "{'10:00:00:00:00:01' : ['RSSI' : -56] }"
mac_address = s3[2:19]
rssiStr = s3[33:36]
rssi = int(rssiStr)
distance = rssi * -0.05

print(mac_address," has", rssi, "dBs, it's","{0:.1f}".format(distance), "meters from BLE antenna")


s3.find("RSSI")
if s3.count("RSSI") <= 3:
    print("ON")
    #MQTT PUBLISH
else:
    print("OFF")
# se debería activar la secuencia de lógicas de presencia en función de la existencia de un "RSSI" en elmensaje principal
# if rssiCount >= 1 then.....
# Para automatizar en f(macType) (macType=x), habrá que hacer un JSON aparte donde especifique el tipo de activo 
if mac_address == "10:00:00:00:00:01" :
    print('UNO está presente')
    if int(rssi) >= -55:
        b = True
        print(b)
else:
    print('NO HAY NÁ')



# Es interesante reconocer la MAC para contar cuántas hay presentes
# Usar el método find(mac_addresses_saved) para hacer lógicas en función de cada una




