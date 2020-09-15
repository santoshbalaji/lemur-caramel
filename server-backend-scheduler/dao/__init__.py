from pymongo import MongoClient

from dao.user import UserDB
from .base import BaseDB
from .operation import OperationDB
from .constants import DATABASE, COLLECTION_SEQUENCE, DATABASE_HOST, DATABASE_PORT

__all__ = ['operation_dao', 'user_dao', 'disconnect_database']


mongo_client = MongoClient(host=DATABASE_HOST, port=DATABASE_PORT)
operation_dao = OperationDB(connection=mongo_client)
user_dao = UserDB(connection=mongo_client)


def disconnect_database():
    mongo_client.close()
