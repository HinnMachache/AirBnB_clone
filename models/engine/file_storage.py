#!/usr/bin/python3
"""File Storage Class, taking care of storage"""

import json
import os


class FileStorage:
    """Private Class Variables"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns Dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects with obj"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes __objects into JSON files"""
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        models = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
                  "Place": Place, "Review": Review, "State": State,
                  "User": User}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                for key, value in json.load(file).items():
                    obj = key.split(".")
                    for tag, data in models.items():
                        if obj[0] == tag:
                            self.new(data(**value))
