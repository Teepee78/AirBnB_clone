#!/usr/bin/python3
"""
This module defines FileStorage Class
"""
import json
from os.path import exists
from datetime import datetime
import copy


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes from a JSON file to instances

    Class Attributes
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects
    """
    __objects = {}
    __file_path = "./models/engine/instances.json"

    def __init__(self):
        pass

    def all(self):
        """returns the dictionary __objects

        Returns:
            a dictionary of objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object to be stored"""

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        # copy dictionary
        copiedDict = dict(FileStorage.__objects)
        for key, instance in copiedDict.items():
            if not isinstance(instance, dict):
                copiedDict[key] = copy.copy(instance).to_dict()
        # convert datetime to isoformat
        for key, instance in copiedDict.items():
            if type(instance["created_at"]) is not str:
                date = instance["created_at"].isoformat()
                instance["created_at"] = date
            if type(instance["updated_at"]) is not str:
                date = instance["updated_at"].isoformat()
                instance["updated_at"] = date

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as wFile:
            if len(FileStorage.__objects) == 0:
                wFile.write("{}")
            else:
                wFile.write(json.dumps(copiedDict))

    def reload(self):
        """deserializes the JSON file to __objects"""

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as rFile:
                from_file = rFile.read()
                if len(from_file) == 0:
                    FileStorage.__objects = {}
                else:
                    FileStorage.__objects = json.loads(from_file)
                    # load instances
                    for key, instance in FileStorage.__objects.items():
                        eval_string = f"{instance['__class__']}(**instance)"
                        FileStorage.__objects[key] = eval(eval_string)
