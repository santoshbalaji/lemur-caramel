import paho.mqtt.client as mqtt
import logging
from service.constants import MQTT_QOS


class MQTTConnection(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.subscribers = {}
        self.client = None

    def _on_connect(self, client: mqtt.Client, userdata: any, rc: any) -> None:
        logging.info("------------------ mqtt connected ----------------" + self.host)

    def _on_message(self, client: mqtt.Client, userdata: any, msg: mqtt.MQTTMessage) -> None:
        logging.info("------------------ mqtt message received -------------" + msg.topic + "---------" + msg.payload)
        if msg.topic in self.subscribers:
            self.subscribers[msg.topic]['callback'](message=msg.payload)

    def publish(self, topic: str, qos: int, message: str) -> None:
        logging.info("--------------- mqtt message for publish ------------" + topic + "-------" + message)
        self.client.publish(topic=topic, qos=qos, payload=message)

    def initialise(self) -> None:
        self.client = mqtt.Client()
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(host=self.host, port=self.port, keepalive=60)
        self.client.subscribe(topic="test", qos=1)
        logging.info("-------------------- mqtt initialised -----------------")

    def subscribe_all(self, subscribers: list) -> None:
        if subscribers and len(subscribers) != 0:
            for subscriber in subscribers:
                self.subscribers[subscriber['topic']] = subscriber
                self.client.subscribe(topic=subscriber['topic'], qos=MQTT_QOS)
        logging.info("-------------- subscribed to topics -------------")

    def close(self) -> None:
        self.client.disconnect()


def test_callback():
    print("works")