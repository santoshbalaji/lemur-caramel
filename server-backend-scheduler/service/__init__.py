from service.connect import MQTTConnection
from service.constants import MQTT_HOST, MQTT_PORT, MQTT_TOPIC_RESULT
from .operation import OperationService

__all__ = ['operation_service', 'OperationService', 'mqtt_connection']

mqtt_connection = MQTTConnection(host=MQTT_HOST, port=MQTT_PORT)
mqtt_connection.initialise()
operation_service = OperationService(mqtt_connection=mqtt_connection)
mqtt_connection.subscribe_all(subscribers=[{'topic': MQTT_TOPIC_RESULT,
                                            'callback': operation_service.get_results}])
