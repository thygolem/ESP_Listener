import os
import json
import time
import datetime
import paho.mqtt.client 


from credentials import CLOUDMQTT_USER, CLOUDMQTT_PASS, CLOUDMQTT_HOST, CLOUDMQTT_PORT

def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))
    time.sleep(0.5)
    print("Conectando")
    time.sleep(0.5)
    print("Conectando")


    # Nos subscribimos al tópico
    client.subscribe('indoor/#', 0)


def on_message(client, userdata, message):
    print("message: " + str(message.topic) + " " + str(message.qos) + " " + str(message.payload))

    # La información que recogemos la trasucimos en json
    payload = json.loads(str(message.payload)[2:-1])
    print(payload)
    time.sleep(0.5)




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
 