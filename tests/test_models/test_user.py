#!/usr/bin/python3
"""
This module contains unittests for UserModel class
"""
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Defines test cases for UserModel class"""

    def test_init(self):
        """Test Initialization"""
        User.email = "abc@gmail.com"
        User.password = "pass"
        User.first_name = "abebe"
        User.last_name = "henok"
        self.assertEqual(User.email, "abc@gmail.com")
        self.assertEqual(User.password, "pass")
        self.assertEqual(User.first_name, "abebe")
        self.assertEqual(User.last_name, "henok")
