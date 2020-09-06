from dao.base import BaseDB
from dao.constants import *
from model import Operation


class OperationDB(BaseDB):
    def create(self, obj: Operation) -> int:
        return self.connection[DATABASE][COLLECTION_OPERATION].insert_one(
            document=obj.convert_to_db_format()).inserted_id

    def update(self, obj: Operation) -> int:
        return self.connection[DATABASE][COLLECTION_OPERATION].update_one(
            filter={'idx': obj.idx}, update={'$set': obj.convert_to_db_format()}).modified_count

    def delete(self, idx: int) -> int:
        return self.connection[DATABASE][COLLECTION_OPERATION].delete_one(filter={'idx': idx}).deleted_count

    def find(self, **params: dict) -> list:
        return [c for c in
                self.connection[DATABASE][COLLECTION_OPERATION].find(**params).sort('current_timestamp', -1)]
