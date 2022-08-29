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
