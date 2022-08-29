#!/usr/bin/env python3
"""
This module defines BaseModel class
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Defines all common attributes/methods for other classes of AirBnB clone

    Attrs:
        id: string - id of instance
        created_at: datetime - datetime when instance was created
        updated_at: datetime - datetime when instance was last updated
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints string representation of instance"""

        string = "BaseModel ({}) {}".format(self.id, self.__dict__)
        return string

    def save(self):
        """Updates 'updated_at' with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """

        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = (self.created_at).isoformat()
        dictionary["updated_at"] = (self.updated_at).isoformat()

        return dictionary
