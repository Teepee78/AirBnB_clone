#!/usr/bin/env python3
"""
This module defines the state class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Defines all attributes related to the State class

    Attrs:
        name: string - name of state
    """
    name = ""
