import abc
from pymongo import MongoClient
from model import Base


class BaseDB(metaclass=abc.ABCMeta):
    def __init__(self, connection: MongoClient):
        self.connection = connection

    @abc.abstractmethod
    def create(self, obj: Base) -> int:
        pass

    @abc.abstractmethod
    def update(self, obj: Base) -> int:
        pass

    @abc.abstractmethod
    def delete(self, idx: int) -> int:
        pass

    @abc.abstractmethod
    def find(self, **params: dict) -> list:
        pass
