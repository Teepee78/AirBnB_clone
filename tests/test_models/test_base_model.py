#!/usr/bin/env python3
"""
This module contains unittests for BaseModel class
"""
from models.base_model import BaseModel
import unittest
import datetime
from time import sleep
from unittest import mock
import uuid


class TestBaseModel(unittest.TestCase):
    """Defines test cases for BaseModel class"""

    maxDiff = None

    def setUp(self):
        self.inst = BaseModel()

    def test_init_none(self):
        """Test initialization"""

        # Testing data type of instance
        self.assertIsInstance(self.inst, BaseModel)

        # Testing if created_at and updated_at are equal upon
        # intialization
        time = datetime.datetime.now().strftime("%H %M %S")
        inst2 = BaseModel()
        self.assertEqual(inst2.created_at.strftime("%H %M %S"), time)
        self.assertEqual(inst2.updated_at.strftime("%H %M %S"), time)

        # Testing attribute data type
        self.assertIsInstance(self.inst.id, str)
        self.assertIsInstance(self.inst.created_at, datetime.datetime)
        self.assertIsInstance(self.inst.updated_at, datetime.datetime)

        # Testing values of attributes (This also checks if all required
        # attributes are present)
        # Mocking datetime.datetime.now() method so that known
        # date is returned
        test_now = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        with mock.patch('datetime.datetime',
                        wraps=datetime.datetime) as dt_mock:
            dt_mock.now.return_value = test_now
            inst3 = BaseModel()
            time = datetime.datetime.now()
            self.assertEqual(inst3.created_at, time)
            self.assertEqual(inst3.updated_at, time)
            # Checing if created_at and updated_at are equal
            self.assertEqual(inst3.created_at, inst3.updated_at)

        # Mocking uuid.uuid4 method so that a known id is returned
        mock_id = uuid.UUID('{b6a6e15c-c67d-4312-9a75-9d084935e579}')
        with mock.patch('uuid.uuid4',
                        wraps=uuid.uuid4) as id_mock:
            dt_mock.now.return_value = test_now
            id_mock.return_value = mock_id
            inst4 = BaseModel()
            self.assertEqual(inst4.id, "b6a6e15c-c67d-4312-9a75-9d084935e579")

        # Adding attributes to instance and checking values
        self.inst.name1 = "Haile Yohannes Ayalew"
        self.inst.name2 = "Johnny"
        self.inst.age = 59
        self.inst.weight = 80.9
        self.assertEqual(self.inst.name1, "Haile Yohannes Ayalew")
        self.assertEqual(self.inst.name2, "Johnny")
        self.assertEqual(self.inst.age, 59)
        self.assertEqual(self.inst.weight, 80.9)

    def test___str___(self):
        """Test output of __str__"""
        # Checking if the format of __str__ is correct
        # Testing without adding additional attributes
        self.assertEqual(self.inst.__str__(), "[BaseModel] ({}) {}"
                         .format(self.inst.id, self.inst.__dict__))

        # Testing by adding new attributes
        self.inst.name = "My First Model"
        self.inst.my_int = 89
        self.inst.my_float = 82.2
        self.assertEqual(self.inst.__str__(), "[BaseModel] ({}) {}"
                         .format(self.inst.id, self.inst.__dict__))

    def test_init_args(self):
        """Test initialization with parameters"""

        with self.assertRaises(TypeError):
            inst = BaseModel(1)
        with self.assertRaises(TypeError):
            inst = BaseModel(1, 2)

    def test_save(self):
        """Test save method"""

        # This function checks if the updated_at is set to the current time
        # when save is called. A mock object is used to generate the current
        # datetime,temporarily this mock object acts like the orginal
        # datetime function and all calls to datetime.now() will be redirected
        # to it.
        test_now = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        with mock.patch('datetime.datetime',
                        wraps=datetime.datetime) as dt_mock:
            dt_mock.now.return_value = test_now
            sleep(2)
            time = datetime.datetime.now()
            self.inst.save()
            self.assertEqual(self.inst.updated_at, time)

            # Checking if the updated_at is not equal to created_at
            inst2 = BaseModel()
            test_now_updated = datetime.datetime(2017, 9, 28, 22, 3, 54, 52298)
            dt_mock.now.return_value = test_now_updated
            inst2.save()
            self.assertNotEqual(inst2.created_at, inst2.updated_at)

    def test_to_dict(self):
        """Test to_dict function"""
        # This test also confirms that the created_at and updated_at
        # are in iso format
        correct_output = {'updated_at': '2017-09-28T21:05:54.119572',
                          'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                          'created_at': '2017-09-28T21:05:54.119572',
                          '__class__': 'BaseModel'}
        # The mock below is done so that we can check
        # the print format of to_dict is correct
        # create mock for datetime
        test_now = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        mock_id = uuid.UUID('{b6a6e15c-c67d-4312-9a75-9d084935e579}')
        with mock.patch('datetime.datetime',
                        wraps=datetime.datetime) as dt_mock:
            with mock.patch('uuid.uuid4',
                            wraps=uuid.uuid4) as id_mock:
                dt_mock.now.return_value = test_now
                id_mock.return_value = mock_id
                inst2 = BaseModel()
                self.assertEqual(inst2.to_dict(), correct_output)
        # Checking type
        self.assertIsInstance(self.inst.to_dict(), dict)
        self.assertIsInstance(self.inst.to_dict()["created_at"], str)
        self.assertIsInstance(self.inst.to_dict()["updated_at"], str)


class TestInstantiateFromDict(unittest.TestCase):
    """Defines test cases for Instantiate from dict"""
    def setUp(self):
        self.dictionary = {
                "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                "created_at": "2017-09-28T21:03:54.052298",
                "__class__": "BaseModel",
                "my_number": 89,
                "updated_at": "2017-09-28T21:03:54.052302",
                "name": "My_First_Model"
                 }
        self.inst = BaseModel(**self.dictionary)

    def test_init_kwargs(self):
        """Test initialization with keyword arguments"""
        self.assertEqual(self.inst.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        self.assertEqual(self.inst.created_at, created_at)
        self.assertEqual(self.inst.my_number, 89)
        updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52302)
        self.assertEqual(self.inst.updated_at, updated_at)
        self.assertEqual(self.inst.name, "My_First_Model")

    def test___class___not_added(self):
        """Test that the __class__ key is not added as attribute"""
        dictionary = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "User",
            "my_number": 89,
            "updated_at": "2017-09-28T21:03:54.052302",
            "name": "My_First_Model"
            }
        inst2 = BaseModel(**dictionary)
        # self.assertRaises(AttributeError):
        self.assertEqual(inst2.__class__.__name__, "BaseModel")

    def test_data_type(self):
        """Test the datatypes of the created_at and updated_at attributes"""
        self.assertIsInstance(self.inst.created_at, datetime.datetime)
        self.assertIsInstance(self.inst.updated_at, datetime.datetime)

    def test_empty_dictionary(self):
        """
        Test if a new instance is initialized
        when an empty dictionary is passed
        """
        test_now = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        mock_id = uuid.UUID('{b6a6e15c-c67d-4312-9a75-9d084935e579}')
        with mock.patch('datetime.datetime',
                        wraps=datetime.datetime) as dt_mock:
            with mock.patch('uuid.uuid4',
                            wraps=uuid.uuid4) as id_mock:
                dt_mock.now.return_value = test_now
                id_mock.return_value = mock_id
                time = datetime.datetime.now()
                dictionary = {}
                inst2 = BaseModel(**dictionary)
                self.assertEqual(inst2.id,
                                 "b6a6e15c-c67d-4312-9a75-9d084935e579")
                self.assertEqual(inst2.created_at, time)
                self.assertEqual(inst2.updated_at, time)


'''
    def test_missing_id(self):
        dictionary = {
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "User",
            "my_number": 89,
            "updated_at": "2017-09-28T21:03:54.052302",
            "name": "My_First_Model"
            }
        inst2 = BaseModel(**dictionary)

    def test_missing_created_at(self):
        dictionary = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "__class__": "User",
            "my_number": 89,
            "updated_at": "2017-09-28T21:03:54.052302",
            "name": "My_First_Model"
            }
        inst2 = BaseModel(**dictionary)

    def test_missing_updated_at(self):
        dictionary = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "User",
            "my_number": 89,
            "name": "My_First_Model"
            }
        inst2 = BaseModel(**dictionary)
'''
