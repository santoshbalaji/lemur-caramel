from enum import Enum


class Status(Enum):
    CREATED = 'created'
    PREPARING = 'preparing'
    EXECUTING = 'executing'
    COMPLETED = 'completed'
