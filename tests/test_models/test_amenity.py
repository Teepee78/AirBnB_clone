#!/usr/bin/python3
"""
This module contains unittests for Amenity class
"""
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Defines test cases for Amenity class"""

    def test_init(self):
        """Test Initialization"""
        inst = Amenity()
        inst.name = "Alberta"
        self.assertEqual(inst.name, "Alberta")
