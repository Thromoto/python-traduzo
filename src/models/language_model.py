from .abstract_model import AbstractModel
from database.db import db


# Req.1
class LanguageModel(AbstractModel):
    _collection = db["users"]

    def __init__(self, data_dict):
        self.data = data_dict

    # Req. 2
    def to_dict(self):
        return ({"name": self.data.get("name", None),
                 "acronym": self.data.get("acronym", None)})

    # Req. 3
    @classmethod
    def list_dicts(cls):
        raise NotImplementedError
