from model import Base


class Sequence(Base):
    def __init__(self, idx: int = 0, collection_name: str = None, sequence_number: int = 0, timestamp: str = None):
        self.idx = idx
        self.collection_name = collection_name
        self.sequence_number = sequence_number
        self.timestamp = timestamp


