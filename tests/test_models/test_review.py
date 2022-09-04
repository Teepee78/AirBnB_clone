#!/usr/bin/python3
"""
This module contains unittests for Review class
"""
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Defines test cases for Review class"""

    def test_init(self):
        """Test Initialization"""
        inst = Review()
        inst.place_id = "11111111-2222-2222-2222-333333888888"
        inst.user_id = "11111111-2222-2222-2222-333333999999"
        inst.text = "random text"
        self.assertEqual(inst.place_id, "11111111-2222-2222-2222-333333888888")
        self.assertEqual(inst.user_id, "11111111-2222-2222-2222-333333999999")
        self.assertEqual(inst.text, "random text")
