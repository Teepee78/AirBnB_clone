#!/usr/bin/python3
"""
This module contains unittests for State class
"""
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Defines test cases for State class"""

    def test_init(self):
        """Test Initialization"""
        inst = State()
        inst.name = "Alberta"
        self.assertEqual(inst.name, "Alberta")
