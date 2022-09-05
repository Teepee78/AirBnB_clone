#!/usr/bin/python3
"""
This module contains unittests for console.py
"""
from console import HBNBCommand
import unittest
import datetime
from unittest import mock
import uuid
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """Defines tests cases for the HBNBCommand class"""

    maxDiff = None
    '''
    def test_do_create(self):
        """Test initialization"""
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create")
    '''
    def test_help(self):
        """Test help"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            self.assertIn("EOF", output)
            self.assertIn("all", output)
            self.assertIn("create", output)
            self.assertIn("destroy", output)
            self.assertIn("help", output)
            self.assertIn("quit", output)
            self.assertIn("show", output)
            self.assertIn("update", output)
