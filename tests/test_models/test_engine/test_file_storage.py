#!/usr/bin/env python3
"""
This module contains unittests for FileStorage class
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
from unittest import mock
import datetime
from os.path import exists
import json


class TestFileStorage(unittest.TestCase):
    """Defines test cases for FileStorage class"""

    # This shows the full difference output incase of failure
    maxDiff = None

    def setUp(self):
        """Sets up common items for the TestFileStorage class"""
        self.store = FileStorage()

    def test_all_and_new(self):
        """Test all method"""

        self.assertIsInstance(self.store, FileStorage)
        obj = self.store.all()
        self.assertIsInstance(obj, dict)
        # checking if the obj instance holds the correct value
        # in the proper format

        dictionary = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "BaseModel",
            "updated_at": "2017-09-28T21:03:54.052302"
            }
        base_inst = BaseModel(**dictionary)
        self.store.new(base_inst)
        obj = self.store.all()
        if "BaseModel.56d43177-cc5f-4d6c-a0c1-e167f8c27337" in obj:
            key_exists = "true"
        else:
            key_exists = "false"
        self.assertEqual(key_exists, "true")
        self.assertIsInstance(list(obj.keys())[0], str)
        value = obj["BaseModel.56d43177-cc5f-4d6c-a0c1-e167f8c27337"]
        self.assertIsInstance(value, BaseModel)
        self.assertEqual(value.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52302)
        self.assertEqual(value.created_at, created_at)
        self.assertEqual(value.updated_at, updated_at)
        self.assertIsInstance(value.created_at, datetime.datetime)
        self.assertIsInstance(value.updated_at, datetime.datetime)

    def test_save_and_reload(self):
        """Test save method"""
        dictionary = {
            "id": "80d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "2022-09-28T21:03:54.052298",
            "__class__": "BaseModel",
            "updated_at": "2022-09-28T21:03:54.052302"
            }
        base_inst = BaseModel(**dictionary)
        self.store.new(base_inst)
        self.assertEqual(exists("./models/engine/instances.json"), True)
        self.store.save()
        self.store.reload()
        obj = self.store.all()
        if "BaseModel.80d43177-cc5f-4d6c-a0c1-e167f8c27337" in obj:
            key_exists = "true"
        else:
            key_exists = "false"
            self.assertEqual(key_exists, "true")
            self.assertIsInstance(list(obj.keys())[0], str)
            value = obj["BaseModel.80d43177-cc5f-4d6c-a0c1-e167f8c27337"]
            self.assertIsInstance(value, BaseModel)
            self.assertEqual(value.id, "80d43177-cc5f-4d6c-a0c1-e167f8c27337")
            created_at = datetime.datetime(2022, 9, 28, 21, 3, 54, 52298)
            updated_at = datetime.datetime(2022, 9, 28, 21, 3, 54, 52302)
            self.assertEqual(value.created_at, created_at)
            self.assertEqual(value.updated_at, updated_at)
            self.assertIsInstance(value.created_at, datetime.datetime)
            self.assertIsInstance(value.updated_at, datetime.datetime)
