#!/usr/bin/python3
"""
This module contains unittests for City class
"""
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Defines test cases for City class"""

    def test_init(self):
        """Test Initialization"""
        inst = City()
        inst.id = "11111111-2222-2222-2222-333333444444"
        inst.name = "lagos"
        self.assertEqual(inst.id, "11111111-2222-2222-2222-333333444444")
        self.assertEqual(inst.name, "lagos")
