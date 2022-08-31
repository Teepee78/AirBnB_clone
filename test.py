#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj, "\n")

# print("-- Create a new object --")
# my_model = BaseModel()
# my_model.name = "My_First_Model"
# my_model.my_number = 89
# my_model.save()
# print(my_model)

# print("-- Create new user --")
# my_user = User()
# my_user.name = "John"
# my_user.number = 90
# my_user.save()
# print(my_user)
