from dao import sequence_dao, operation_dao, user_dao
from model import Operation, Status
from service.base import BaseService
from service.constants import SEQUENCE_COLLECTION_OPERATION
from datetime import datetime
from service.message import Message, Error
import logging


class OperationService(BaseService):
    def create_operation(self, operation: dict) -> (int, str):
        try:
            if not self._validate_user_id(user_id=operation['user_id']):
                logging.error(Error.ERROR_OPERATION_USER_NOT_EXISTS.format(operation['user_id']))
                return 409, Error.ERROR_OPERATION_USER_NOT_EXISTS.format(operation['user_id'])
            operation = Operation(**operation)
            operation.idx = sequence_dao.increment_and_get_sequence(SEQUENCE_COLLECTION_OPERATION)
            operation.status = Status.CREATED.value
            operation.created_timestamp = str(datetime.now())
            operation_dao.create(obj=operation)
            logging.info(Message.OPERATION_CREATED.format(operation.idx))
            return 200, Message.OPERATION_CREATED.format(operation.idx)
        except Exception as e:
            logging.error(Error.ERROR_OPERATION_CREATE.format(str(e)))
            return 500, Error.ERROR_OPERATION_CREATE.format(str(e))

    def get_all_operations(self, operation_status: str) -> (int, any):
        try:
            if operation_status and len(operation_status) != 0:
                return 200, operation_dao.find(**{'filter': {'status': operation_status}, 'projection': {'_id': 0}})
            else:
                return 200, operation_dao.find(**{'filter': {}, 'projection': {'_id': 0}})
        except Exception as e:
            logging.error(Error.ERROR_OPERATION_GET.format(str(e)))
            return 500, Error.ERROR_OPERATION_GET.format(str(e))

    @staticmethod
    def _validate_user_id(user_id: int) -> bool:
        return len(user_dao.find(**{'filter': {'idx': user_id}})) != 0

    @staticmethod
    def _validate_operation_id(operation_id: int) -> (bool, any):
        operations = operation_dao.find(**{'filter': {'idx': operation_id}})
        return (True, operations[0]) if len(operations) != 0 else (False, None)
