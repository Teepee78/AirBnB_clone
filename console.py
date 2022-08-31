#!/usr/bin/env python3
"""Entry point of the command interpreter"""
import cmd
import json
import re
from models.base_model import BaseModel
from models import storage
from models.user import User


# List of classes
classes = [
    "BaseModel",
    "User"
]

jsonpath = "models/engine/instances.json"


# Parser function to validate commands
def parser(argv):
    """Validate command line arguments

    Returns:
        list of command line arguments or None if invalid commands
    """
    if len(argv) == 0:
        print("** class name missing **")
        return
    # Split argv into a list of strings
    args = argv.split()
    # Check if class exists
    if args[0] not in classes:
        print("** class doesn't exist **")
        return
    return args


class HBNBCommand(cmd.Cmd):
    """Contains functions for command interpreter"""
    prompt = "(hbnb) "

    def do_create(self, argv):
        """
        Creates a new instance of a class,
        saves it to JSON file and prints ID
        """

        args = parser(argv)
        if args is None:
            return
        instance = eval(f"{args[0]}()")
        # save to json file
        storage.new(instance)
        storage.save()
        print(instance.id)

    def do_show(self, argv):
        """
        Prints the sting representation of an instance based on the
        class name and id
        """

        args = parser(argv)
        if args is None:
            return
        if len(args) == 1:  # id is missing
            print("** instance id missing **")
            return
        # Get all instances
        instances = storage.all()

        # Search instances
        for key, instance in instances.items():
            search = f"{args[0]}.{args[1]}"
            if search == key:
                # create instance
                inst = eval(f"{args[0]}(**instance)")
                print(inst)
                return
        print("** no instance found **")

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id"""
        args = parser(argv)
        if args is None:
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instances = storage.all()

        for key, instance in instances.items():
            search = f"{args[0]}.{args[1]}"
            if search == key:
                # The item is deleted here
                # It is directly deleted from the instances variable since
                # dictionaries are passed by reference instances referes to
                # the original __objects dictionary
                instances.pop(search)
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, argv):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        inst_str_list = []
        # Case 1: Argument is not provided
        if len(argv) == 0:
            instances = storage.all()
            for key, instance in instances.items():
                # Checking and converting new instances to a dictionary
                if not isinstance(instance, dict):
                    instance = instance.to_dict()
                # create instance
                inst = eval(f"{instance['__class__']}(**instance)")
                inst_str_list.append(inst.__str__())
            print(inst_str_list)
            return
        args = argv.split()
        # Check if classes exists
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        # Case 2: Argument is provided
        inst_str_list = []
        instances = storage.all()
        for key, instance in instances.items():
            # Checks if the key contains the name of the class
            if re.search(f"{args[0]}{'.'}.*", key):
                # Checking and converting new instances to a dictionary
                if not isinstance(instance, dict):
                    instance = instance.to_dict()
                # create instance
                inst = eval(f"{args[0]}(**instance)")
                inst_str_list.append(inst.__str__())
        print(inst_str_list)

    def do_quit(self, argv):
        """Quits command interpreter"""

        return True

    def do_EOF(self, argv):
        """End of File, exits command interpreter"""

        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
