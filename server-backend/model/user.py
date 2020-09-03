from model import Base


class User(Base):
    def __init__(self, idx: int = 0, uuid: str = None, session_id: str = None, timestamp: str = None):
        self.idx = idx
        self.uuid = uuid
        self.session_id = session_id
        self.timestamp = timestamp


