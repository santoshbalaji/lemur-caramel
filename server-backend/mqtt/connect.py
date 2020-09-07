import paho.mqtt.client as mqtt


class MqttConnection(object):
    def __init__(self, host: str, port: int):
        self.client = mqtt.Client()
        self.client.connect(host=host, port=port)
