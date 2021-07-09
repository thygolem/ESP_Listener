import os
import json
import time
import datetime
import paho.mqtt.client 


from mongoengine import connect
from config import MONGODB_USER, MONGODB_PASSWORD,MONGODB_URI, CLOUDMQTT_USER, CLOUDMQTT_PASS, CLOUDMQTT_HOST, CLOUDMQTT_PORT

connect(username=MONGODB_USER, password=MONGODB_PASSWORD, host=MONGODB_URI)

def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

    # Nos subscribimos al tópico
    client.subscribe('indoor/#', 0)
 
def on_message(client, userdata, message):
    print("message: " + str(message.topic) + " " + str(message.qos) + " " + str(message.payload))

    # La información que recogemos la trasucimos en json
    payload = json.loads(str(message.payload)[2:-1])

    # Tomamos el gateway
    if len(payload) > 0:
        gateway = payload[0]
    if len(payload) >= 2:
        for device in payload[1:]:
            mac = device['mac']
            rssi = device['rssi']
            if mac == 'CC11FA17965D':
                if -50 >= rssi >= -60:
                    device_data = DeviceData(d_mac=device['mac'], g_mac=gateway['mac'], bleName=device['bleName'],
                                            rssi=device['rssi'], rawData=device['rawData'], in_zone=True,
                                            timestamp=datetime.datetime.utcnow())
                    device_data.save()
                else:
                    device_data = DeviceData(d_mac=device['mac'], g_mac=gateway['mac'], bleName=device['bleName'],
                                            rssi=device['rssi'], rawData=device['rawData'],
                                            timestamp=datetime.datetime.utcnow())
                    device_data.save()

def main():
    # Conectamos con el broker mqtt
    client = paho.mqtt.client.Client(client_id='winder', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(CLOUDMQTT_USER, CLOUDMQTT_PASS)
    client.connect(host=CLOUDMQTT_HOST, port=CLOUDMQTT_PORT, keepalive=60)
    client.loop_forever()

if __name__ == '__main__':
    main()
 
