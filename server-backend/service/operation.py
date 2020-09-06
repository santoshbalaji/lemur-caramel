from dao import sequence_dao, operation_dao, user_dao
from model import Operation, Status
from service.base import BaseService
from service.constants import SEQUENCE_COLLECTION_OPERATION
from datetime import datetime
from service.message import Message, Error


class OperationService(BaseService):
    def create_operation(self, operation: dict) -> str:
        try:
            if not self._validate_user_id(user_id=operation['user_id']):
                self.logging.error(Error.ERROR_OPERATION_USER_NOT_EXISTS.format(operation['user_id']))
                return Error.ERROR_OPERATION_USER_NOT_EXISTS.format(operation['user_id'])
            operation = Operation(**operation)
            operation.idx = sequence_dao.increment_and_get_sequence(SEQUENCE_COLLECTION_OPERATION)
            operation.status = Status.CREATED.value
            operation.created_timestamp = str(datetime.now())
            operation_dao.create(obj=operation)
            self.logging.info(Message.OPERATION_CREATED.format(operation.idx))
            return Message.OPERATION_CREATED.format(operation.idx)
        except Exception as e:
            self.logging.error(Error.ERROR_OPERATION_CREATE.format(str(e)))
            return Error.ERROR_OPERATION_CREATE.format(str(e))

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

    def get_all_operations(self, operation_status: str) -> any:
        try:
            if operation_status and len(operation_status) != 0:
                return operation_dao.find(**{'filter': {'status': operation_status}})
            else:
                return operation_dao.find(**{'filter': {}})
        except Exception as e:
            self.logging.error(Error.ERROR_OPERATION_GET.format(str(e)))
            return Error.ERROR_OPERATION_GET.format(str(e))

    def get_next_operation(self) -> any:
        try:
            operations = operation_dao.find(**{'filter': {'status': Status.CREATED.value}})
            return operations[0] if len(operations) != 0 else None
        except Exception as e:
            self.logging.error(Error.ERROR_OPERATION_GET.format(str(e)))
            return Error.ERROR_OPERATION_GET.format(str(e))

    @staticmethod
    def _validate_user_id(user_id: int) -> bool:
        return len(user_dao.find(**{'filter': {'id': user_id}})) != 0

    @staticmethod
    def _validate_operation_id(operation_id: int) -> (bool, any):
        operations = operation_dao.find(**{'filter': {'id': operation_id}})
        return (True, operations[0]) if len(operations) != 0 else (False, None)
