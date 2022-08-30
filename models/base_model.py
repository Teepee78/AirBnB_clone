#!/usr/bin/env python3
"""
This module defines BaseModel class
"""
from datetime import datetime
from uuid import uuid4
from __init__ import storage


class BaseModel:
    """
    Defines all common attributes/methods for other classes of AirBnB clone

    Attrs:
        id: string - id of instance
        created_at: datetime - datetime when instance was created
        updated_at: datetime - datetime when instance was last updated
    """

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    date = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, date)
                else:
                    setattr(self, key, value)
        elif len(args) != 0:
            raise TypeError("Too many arguments")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Prints string representation of instance"""

        string = "[BaseModel] ({}) {}".format(self.id, self.__dict__)
        return string

    def save(self):
        """Updates 'updated_at' with the current datetime"""

        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """

        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
