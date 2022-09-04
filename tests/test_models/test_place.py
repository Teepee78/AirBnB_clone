#!/usr/bin/python3
"""
This module contains unittests for Place class
"""
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Defines test cases for Place class"""

    def test_init(self):
        """Test Initialization"""
        inst = Place()
        inst.city_id = "11111111-2222-2222-2222-333333888888"
        inst.user_id = "11111111-2222-2222-2222-333333999999"
        inst.name = "Bole"
        inst.description = "random description"
        inst.amenity_ids = ["Bole"]
        self.assertEqual(inst.city_id, "11111111-2222-2222-2222-333333888888")
        self.assertEqual(inst.user_id, "11111111-2222-2222-2222-333333999999")
        self.assertEqual(inst.name, "Bole")
        self.assertEqual(inst.description, "random description")
        self.assertEqual(inst.number_rooms, 0)
        self.assertEqual(inst.number_bathrooms, 0)
        self.assertEqual(inst.max_guest, 0)
        self.assertEqual(inst.price_by_night, 0)
        self.assertEqual(inst.latitude, 0.0)
        self.assertEqual(inst.longitude, 0.0)
        self.assertEqual(inst.amenity_ids[0], "Bole")
