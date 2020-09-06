from dao import sequence_dao, user_dao
from model import User
from service.base import BaseService
from service.constants import SEQUENCE_COLLECTION_USER
from service.message import Error, Message
from datetime import datetime


class UserService(BaseService):
    def create_user(self, user: dict) -> (int, str):
        try:
            user = User(**user)
            user.idx = sequence_dao.increment_and_get_sequence(SEQUENCE_COLLECTION_USER)
            user.created_timestamp = str(datetime.now())
            user_dao.create(obj=user)
            self.logging.info(Message.USER_CREATED.format(user.idx))
            return 200, Message.USER_CREATED.format(user.idx)
        except Exception as e:
            self.logging.error(Error.ERROR_USER_CREATE.format(str(e)))
            return 500, Error.ERROR_USER_CREATE.format(str(e))

    def get_users(self, user_id: any) -> (int, any):
        try:
            if user_id is not None:
                return 200, user_dao.find(**{'filter': {'user_id': user_id}, 'projection': {'_id': 0}})
            else:
                return 200, user_dao.find(**{'filter': {}, 'projection': {'_id': 0}})
        except Exception as e:
            self.logging.error(Error.ERROR_USER_GET.format(str(e)))
            return 500, Error.ERROR_USER_GET.format(str(e))
