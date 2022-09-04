#!/usr/bin/env python3
"""
This module defines the city class
"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """
    Defines all attributes related to the City class

    Attrs:
        state_id: string - id of state
        name: string - name of state
    """
    state_id = ""
    name = ""
