import json
from dao import operation_dao, user_dao
from .constants import MQTT_TOPIC_COMMAND, MQTT_QOS
from model import Operation, Status
from service.base import BaseService
from datetime import datetime
from service.message import Message, Error


class OperationService(BaseService):
    def update_operation_status(self, operation_id: int, operation_status: str) -> str:
        try:
            status, operation = self._validate_operation_id(operation_id=operation_id)
            if not status:
                self.logging.error(Error.ERROR_OPERATION_NOT_EXISTS.format(operation_id))
                return Error.ERROR_OPERATION_NOT_EXISTS.format(operation_id)
            operation = Operation(**operation)
            operation.status = operation_status
            operation.updated_timestamp = str(datetime.now())
            operation_dao.update(obj=operation)
            self.logging.info(Message.OPERATION_UPDATED.format(operation.idx))
            return Message.OPERATION_UPDATED.format(operation.idx)
        except Exception as e:
            self.logging.error(Error.ERROR_OPERATION_UPDATE.format(str(e)))
            return Error.ERROR_OPERATION_UPDATE.format(str(e))

    def get_next_operation(self) -> any:
        try:
            running_operations = operation_dao.find(**{'filter': {'status': {'$nin': [Status.CREATED.value,
                                                                                      Status.COMPLETED.value]}}})
            if not running_operations or len(running_operations) == 0:
                operations = operation_dao.find(**{'filter': {'status': Status.CREATED.value}, 'projection': {'_id': 0}})
                if operations and len(operations) != 0:
                    operations[0]['operation_id'] = operations[0]['idx']
                    self.mqtt_connection.publish(topic=MQTT_TOPIC_COMMAND, qos=MQTT_QOS, message=json.dumps(operations[0]))
                    self.update_operation_status(operation_id=operations[0]['idx'],
                                                 operation_status=Status.PREPARING.value)
                    return operations[0]
                else:
                    return None
        except Exception as e:
            self.logging.error(Error.ERROR_OPERATION_GET_NEXT_JOB.format(str(e)))
            return Error.ERROR_OPERATION_GET_NEXT_JOB.format(str(e))

    def get_results(self, message: str) -> any:
        try:
            iot_ops = json.loads(message)
            if iot_ops and 'operation_id' in iot_ops and 'status' in iot_ops:
                operations = operation_dao.find(**{'filter': {'idx': iot_ops['operation_id']}})
                if operations and len(operations) != 0:
                    users = user_dao.find(**{'filter': {'idx': operations[0]['user_id']}})
                    self.mqtt_connection.publish(topic=users[0]['topic'], qos=MQTT_QOS,
                                                 message=json.dumps({'status': iot_ops['status']}))
                    self.update_operation_status(operation_id=operations[0]['id'], operation_status=iot_ops['status'])
        except Exception as e:
            self.logging.error(Error.ERROR_OPERATION_GET_RESULT.format(str(e)))
            return Error.ERROR_OPERATION_GET_RESULT.format(str(e))

    @staticmethod
    def _validate_operation_id(operation_id: int) -> (bool, any):
        operations = operation_dao.find(**{'filter': {'idx': operation_id}, 'projection': {'_id': 0}})
        return (True, operations[0]) if len(operations) != 0 else (False, None)
