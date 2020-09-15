import logging


class BaseService(object):
    def __init__(self):
        logging.basicConfig(filename='logs/backend.log')
        self.logging = logging
