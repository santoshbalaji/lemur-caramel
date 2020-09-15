from pymongo import MongoClient
from .base import BaseDB
from .operation import OperationDB
from .sequence import SequenceDB
from .user import UserDB
from .constants import DATABASE, COLLECTION_SEQUENCE

__all__ = ['operation_dao', 'user_dao', 'sequence_dao']


mongo_client = MongoClient(host='localhost', port=27017)
operation_dao = OperationDB(connection=mongo_client)
user_dao = UserDB(connection=mongo_client)
sequence_dao = SequenceDB(connection=mongo_client)

mongo_client.drop_database(DATABASE)
mongo_client[DATABASE][COLLECTION_SEQUENCE].insert_one({'idx': 1, 'sequence_number': 1, 'collection_name': 'operation'})
mongo_client[DATABASE][COLLECTION_SEQUENCE].insert_one({'idx': 2, 'sequence_number': 1, 'collection_name': 'user'})
