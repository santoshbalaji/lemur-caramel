import logging


class BaseService(object):
    def __init__(self):
        logging.basicConfig(filename='backend.log')
        self.logging = logging
