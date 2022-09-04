#!/usr/bin/env python3
"""
This module defines the Review class
"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """
    Defines all attributes related to the Review

    Attrs:
        place_id: string - id of place
        user_id: string - id of user
        text: string - review text
    """

    place_id = ""
    user_id = ""
    text = ""
