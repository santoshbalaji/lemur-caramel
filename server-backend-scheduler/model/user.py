from model import Base


class User(Base):
    def __init__(self, idx: int = 0, user_id: int = None, topic: str = None,
                 created_timestamp: str = None, updated_timestamp: str = None):
        self.idx = idx
        self.user_id = user_id
        self.topic = topic
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
