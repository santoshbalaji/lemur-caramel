from dao import BaseDB
from dao.constants import DATABASE, COLLECTION_USER
from model import User


class UserDB(BaseDB):
    def create(self, obj: User) -> int:
        return self.connection[DATABASE][COLLECTION_USER].insert_one(document=obj.convert_to_db_format()).inserted_id

    def update(self, obj: User) -> int:
        return self.connection[DATABASE][COLLECTION_USER].update_one(
            filter={'idx': obj.convert_to_db_format()}, update={'$set': obj.convert_to_db_format()}).modified_count

    def delete(self, idx: int) -> int:
        return self.connection[DATABASE][COLLECTION_USER].delete_one(filter={'idx': idx}).deleted_count

    def find(self, **params: dict) -> list:
        return [c for c in self.connection[DATABASE][COLLECTION_USER].find(**params)]
