import json


class Base(object):
    def get_json_str(self) -> str:
        return json.dumps(self.__dict__)

    def convert_to_obj(self, json_str: str) -> None:
        self.__dict__ = json.loads(json_str)

    def convert_to_db_format(self) -> dict:
        return self.__dict__

