from dao import sequence_dao, user_dao
from model import User
from service.base import BaseService
from service.constants import SEQUENCE_COLLECTION_USER
from service.message import Error
from datetime import datetime
import logging


class UserService(BaseService):
    def create_user(self, user: dict) -> (int, str):
        try:
            user = User(**user)
            user.idx = sequence_dao.increment_and_get_sequence(SEQUENCE_COLLECTION_USER)
            user.topic = 'frontend-' + str(user.idx) + "-" + str(user.user_id)
            user.created_timestamp = str(datetime.now())
            user_dao.create(obj=user)
            del user.__dict__['_id']
            return 200, user.convert_to_db_format()
        except Exception as e:
            logging.error(Error.ERROR_USER_CREATE.format(str(e)))
            return 500, Error.ERROR_USER_CREATE.format(str(e))

    def get_users(self, user_id: any) -> (int, any):
        try:
            if user_id is not None:
                return 200, user_dao.find(**{'filter': {'user_id': user_id}, 'projection': {'_id': 0}})
            else:
                return 200, user_dao.find(**{'filter': {}, 'projection': {'_id': 0}})
        except Exception as e:
            logging.error(Error.ERROR_USER_GET.format(str(e)))
            return 500, Error.ERROR_USER_GET.format(str(e))
