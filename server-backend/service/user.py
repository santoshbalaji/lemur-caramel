from dao import sequence_dao, user_dao
from model import User
from service.base import BaseService
from service.constants import SEQUENCE_COLLECTION_USER
from service.message import Error, Message
from datetime import datetime


class UserService(BaseService):
    def create_user(self, user: dict) -> str:
        try:
            user = User(**user)
            user.idx = sequence_dao.increment_and_get_sequence(SEQUENCE_COLLECTION_USER)
            user.created_timestamp = str(datetime.now())
            user_dao.create(obj=user)
            self.logging.info(Message.USER_CREATED.format(user.idx))
            return Message.USER_CREATED.format(user.idx)
        except Exception as e:
            self.logging.error(Error.ERROR_USER_CREATE.format(str(e)))
            return Error.ERROR_USER_CREATE.format(str(e))

    def get_all_users(self) -> any:
        try:
            return user_dao.find(**{'filter': {}})
        except Exception as e:
            self.logging.error(Error.ERROR_USER_GET.format(str(e)))
            return Error.ERROR_USER_GET.format(str(e))
