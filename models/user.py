#!/usr/bin/python3
"""
This module defines the class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines attributes for user

    Attrs:
        email: string - email of user
        password: string - password of user
        first_name: string - first_name of user
        last_name: string - last_name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
