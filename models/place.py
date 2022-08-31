#!/usr/bin/env python3
"""
This module defines the place class
"""


class Place(BaseModel):
    """
    Defines all attributes related to the Place class

    Attrs:
        city_id: string - id of city
        user_id: string - id of user
        name: string - name of place
        description: string - description of place
        number_rooms: int - number of rooms
        number_bathrooms: int - number of bathrooms
        max_guest: int - max number of guests
        price_by_night: int - price per night
        latitude: float - latitude of place
        longitude: float - longitude of place
        amenity_ids: list - list of amenity ids
    """
    city_id = ""   # City.id
    user_id = ""   # User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtitude = 0.0
    amenity_ids = []
    def __init__(self)
    """Initializer for Place Class"""
    {
            pass
    }
