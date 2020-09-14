from service.operation import OperationService
from service.user import UserService

__all__ = ['operation_service', 'user_service']

operation_service = OperationService()
user_service = UserService()
