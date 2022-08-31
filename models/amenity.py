#!/usr/bin/env python3
"""
This module defines the amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines all attributes related to the Amenity class

    Class Attrs:
        name: string - name of amenity
    """

    name = ""
