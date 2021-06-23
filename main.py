#import paho para usar MQTT 
#import mongoengine para guardar en DB


#import pandas para mapas de calor sobre imagen ?? valdría para análisis,
# pero la representación debe de ser en tº real en javacript web + phas3r


#estudiar la viabilidad de usar docker-compose.yml para ejecutar el entorno web y el script de python

# El stack sería Python=Backend, JS=Frontend. Sin embargo, quizás sea interesante realizar las lógicas de activación en JS y con WebSockets

a = 0
b = None

s3 = "{'10:00:00:00:00:01' : ['RSSI' : -56] }"

mac_address = s3[2:19]
rssiStr = s3[33:36]

rssi = int(rssiStr)
distance = rssi * -0.05
print(mac_address," has", rssi, "dBs, it's","{0:.1f}".format(distance), "meters from BLE antenna")


if mac_address == "10:00:00:00:00:01" :
    print('Uno está presente')
    print(type(rssi))
    if int(rssi) >= -55:
        b = True
        print(b)
        s3.count("RSSI")
else:
    print('NO HAY NÁ')



s3.find("RSSI")
if s3.count("RSSI") <= 3:
    print("ON")
else:
    print("OFF")

#s3.count("10:00:00:00:00:01")
#mac_address.split(":")
# Hay que saber reconocer el formato de MAC ADDRESS para los str() del ESP32 para guardar el dato del RSSI corresponiente
# Es interesante reconocer la MAC para contar cuántas hay presentes
#Usar el método find(mac_addresses_saved) para hacer lógicas en función de cada una




