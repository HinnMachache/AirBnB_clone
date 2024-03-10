#!/usr/bin/python3
"""This is the base Model"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defining the class constructor"""
    def __init__(self, *args, **kwargs):
        """If the class constructor is empty handle it"""
        if len(kwargs) > 0:
            """Iterate through kwargs"""
            for key, value in kwargs.items():
                """Take care of date formats"""
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            """Assign ID"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns String Representation of the object"""
        dic = {}
        for key, value in self.__dict__.items():
            dic[key] = value
        class_name = self.__class__.__name__
        return "[" + class_name + "] " + "(" + self.id + ") " + str(dic)

    def save(self):
        """Save Information to storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary represntation"""
        dic = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dic[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dic[key] = value
        dic["__class__"] = type(self).__name__
        return dic
