from pymongo import MongoClient
from .base import BaseDB
from .operation import OperationDB
from .sequence import SequenceDB
from .user import UserDB


__all__ = ['operation_dao', 'user_dao', 'sequence_dao']


mongo_client = MongoClient('localhost', 27017)
operation_dao = OperationDB(connection=mongo_client)
user_dao = UserDB(connection=mongo_client)
sequence_dao = SequenceDB(connection=mongo_client)
