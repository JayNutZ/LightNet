import paho.mqtt.client as mqtt
import json


class MqttWatcher:
    config = {
        "mqtt": {
            "host": "YOUR IP",
            "user": "MQTT USER",
            "password": "MQTT PASSWORD",
            "full_topic": "MQTT TOPIC"
        }
    }

    client = None

    def __init__(self):
        self.run()
    
    def run(self):
        self.client = mqtt.Client("MQTT")

        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.notified
        self.client.on_log = self.log

        self.client.username_pw_set(self.config['mqtt']['user'], self.config['mqtt']['password'])
        self.client.connect(self.config['mqtt']['host'])

        self.client.loop_forever()

    def subscribe(self):
        self.client.subscribe(self.config['mqtt']['full_topic'] + "/set")

    def send_state(self):
        self.client.publish(self.config['mqtt']['full_topic'], self.payload)

    def connected(self, client, userdata, flags, rc):
        print("MQTT connected")

        self.subscribe()

    def disconnected(self, client, userdata, rc):
        print("MQTT disconnected")

    def notified(self, client, userdata, message):
        print("MQTT MSG: " + json.dumps(json.loads(message.payload)))

    def log(self, mqttc, obj, level, string):
        print("MQTT log: " + string)

if __name__ == '__main__':
    light_mqtt = MqttWatcher()
set