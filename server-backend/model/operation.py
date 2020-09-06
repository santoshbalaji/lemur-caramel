import json

from model import Base


class Operation(Base):
    def __init__(self, idx: int = 0, user_id: int = 0, operation: str = None, parameters: dict = None,
                 status: str = None, created_timestamp: str = None, updated_timestamp: str = None):
        self.idx = idx
        self.user_id = user_id
        self.operation = operation
        self.parameters = parameters
        self.status = status
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
