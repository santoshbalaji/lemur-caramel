from dao import BaseDB
from dao.constants import DATABASE, COLLECTION_SEQUENCE
from model import Sequence


class SequenceDB(BaseDB):
    def create(self, obj: Sequence) -> int:
        return self.connection[DATABASE][COLLECTION_SEQUENCE].insert_one(
            document=obj.convert_to_db_format()).inserted_id

    def update(self, obj: Sequence) -> int:
        return self.connection[DATABASE][COLLECTION_SEQUENCE].update_one(
            filter={'idx': obj.convert_to_db_format()}, update={'$set': obj.convert_to_db_format()}).modified_count

    def delete(self, idx: int) -> int:
        return self.connection[DATABASE][COLLECTION_SEQUENCE].delete_one(filter={'idx': idx}).deleted_count

    def find(self, **params: dict) -> list:
        return [Sequence(**c) for c in self.connection[DATABASE][COLLECTION_SEQUENCE].find(params, {'_id': 0})]

    def increment_and_get_sequence(self, collection_name: str) -> dict:
        return self.connection[DATABASE][COLLECTION_SEQUENCE].find_one_and_update(
            filter={'collection_name': collection_name}, update={'$inc': {'sequence_number': 1}})
