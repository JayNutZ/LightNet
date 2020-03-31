import paho.mqtt.client as mqtt
import json
import atexit
import time
from lgtt_payload import LgttPayload


class LGTT:
    config = {
        "mqtt": {
            "host": "YOUR IP",
            "user": "MQTT USER",
            "password": "MQTT PASSWORD",
            "full_topic": "MQTT TOPIC"
        }
    }

    payload = '{"state": "ON", "brightness": 255}'

    client = None

    def __init__(self):
        print("LGTT start")
        self.run()
    
    def run(self):
        self.client = mqtt.Client("LGTT")

        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.notified
        self.client.on_log = self.log

        self.client.username_pw_set(self.config['mqtt']['user'], self.config['mqtt']['password'])
        self.client.connect(self.config['mqtt']['host'])

        self.send_state()

        self.client.loop_forever()

    def subscribe(self):
        print("LGTT subscribe: " + self.config['mqtt']['full_topic'])
        self.client.subscribe(self.config['mqtt']['full_topic'] + "/set")

    def send_state(self):
        print("LGTT state: " + self.payload)
        self.client.publish(self.config['mqtt']['full_topic'], self.payload)

    def connected(self, client, userdata, flags, rc):
        print("LGTT connection: " + ("success" if rc == 0 else "failed - " + str(rc)))

        self.subscribe()

    def disconnected(self, client, userdata, rc):
        print("LGTT disconnected - " + str(rc))

    def notified(self, client, userdata, message):
        print("LGTT notification: " + str(message.payload))

        payload = LgttPayload(message.payload)

        self.payload = payload.json_string()

        self.send_state()

    def stop():
        print("LGTT stop")
        self.client.loop_stop()
        self.client.disconnect()

    def log(self, mqttc, obj, level, string):
        print("LGTT log: " + string + " (" + str(level) + ")")

if __name__ == '__main__':
    light_mqtt = LGTT()

    atexit.register(light_mqtt.stop)