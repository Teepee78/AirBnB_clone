#!/usr/bin/python3
"""
This module contains unittests for BaseModel class
"""
from models.user import User
import unittest


class TestUserModel(unittest.TestCase):
    """Defines test cases for UserModel class"""

    def test_init(self):
        """Test Initialization"""
        inst = User()
        inst.email = "abc@gmail.com"
        inst.password = "pass"
        inst.first_name = "abebe"
        inst.last_name = "henok"
        self.assertEqual(inst.email, "abc@gmail.com")
        self.assertEqual(inst.password, "pass")
        self.assertEqual(inst.first_name, "abebe")
        self.assertEqual(inst.last_name, "henok")
