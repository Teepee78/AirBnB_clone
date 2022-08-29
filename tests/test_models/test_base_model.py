#!/usr/bin/env python3
"""
This module contains unittests for BaseModel class
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Defines test cases for BaseModel class"""

    def test_init_none(self):
        """Test initialization"""

        inst = BaseModel()
        self.assertIsInstance(inst, BaseModel)
        time = datetime.now().strftime("%H %M %S")
        inst2 = BaseModel()
        self.assertEqual(inst2.created_at.strftime("%H %M %S"), time)
        self.assertEqual(inst2.updated_at.strftime("%H %M %S"), time)

    def test_init_kwargs(self):
        """Test initialization with keyword arguments"""

        dictionary = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "BaseModel",
            "my_number": 89,
            "updated_at": "2017-09-28T21:03:54.052302",
            "name": "My_First_Model"
        }
        inst = BaseModel(**dictionary)
        self.assertEqual(inst.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        created_at = datetime(2017, 9, 28, 21, 3, 54, 52298)
        self.assertEqual(inst.created_at, created_at)
        self.assertEqual(inst.my_number, 89)
        updated_at = datetime(2017, 9, 28, 21, 3, 54, 52302)
        self.assertEqual(inst.updated_at, updated_at)
        self.assertEqual(inst.name, "My_First_Model")

    def test_init_args(self):
        """Test initialization with parameters"""

        with self.assertRaises(TypeError):
            inst = BaseModel(1)
        with self.assertRaises(TypeError):
            inst = BaseModel(1, 2)

    def test_save(self):
        """Test save method"""

        inst = BaseModel()
        sleep(2)
        time = datetime.now().strftime("%H %M %S")
        inst.save()
        self.assertEqual(inst.updated_at.strftime("%H %M %S"), time)

    def test_to_dict(self):
        """Test to_dict function"""

        inst = BaseModel()
        self.assertIsInstance(inst.to_dict(), dict)
