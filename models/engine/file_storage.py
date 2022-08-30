#!/usr/bin/env python3
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
    __file_path = ".models/engine/instances.json"

    def __init__(self):
        pass

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        # copy dictionary
        for key, instance in FileStorage.__objects.items():
            if not isinstance(instance, dict):
                FileStorage.__objects[key] = copy.copy(instance).to_dict()
        copiedDict = dict(FileStorage.__objects)
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

        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as rFile:
                from_file = rFile.read()
                if len(from_file) == 0:
                    FileStorage.__objects = {}
                else:
                    FileStorage.__objects = json.loads(from_file)
            # convert dates to datetime
            for key, instance in FileStorage.__objects.items():
                format = '%Y-%m-%dT%H:%M:%S.%f'
                # convert created_at
                created_at = datetime.strptime(instance["created_at"], format)
                instance["created_at"] = created_at
                # convert updated_at
                updated_at = datetime.strptime(instance["updated_at"], format)
                instance["updated_at"] = updated_at
