import logging

from service.connect import MQTTConnection


class BaseService(object):
    def __init__(self, mqtt_connection: MQTTConnection):
        self.logging = logging
        self.mqtt_connection = mqtt_connection
