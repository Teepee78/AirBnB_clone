#!/usr/bin/env python3
"""Entry point of the command interpreter"""
import cmd
import json
import re
from models.base_model import BaseModel
from models import storage


# List of classes
classes = [
    "BaseModel"
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
        instance = BaseModel()
        # save to json file
        storage.save()
        print(instance.id)

    def do_show(self, argv):
        """
        Prints the string representation of an instance based on the
        class name and id
        """

        args = parser(argv)
        if args is None:
            return
        if len(args) == 1:  # id is missing
            print("** instance id missing **")
            return
        # Get all instances
        storage.reload()
        instances = storage.all()

        # Search instances
        for key, instance in instances.items():
            search = f"{args[0]}.{args[1]}"
            if search == key:
                # create instance
                inst = BaseModel(**instance)
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
        storage.reload()
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
            storage.reload()
            instances = storage.all()
            for key, instance in instances.items():
                inst = BaseModel(**instance)
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
        storage.reload()
        instances = storage.all()
        for key, instance in instances.items():
            # Checks if the key contains the name of the class
            if re.search(f"{args[0]}{'.'}.*", key):
                inst = BaseModel(**instance)
                inst_str_list.append(inst.__str__())
        print(inst_str_list)

    def do_update(self, argv):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = parser(argv)
        if len(args) == 3:  # attribute value is missing
            print("** value missing **")
            return
        if len(args) == 2:  # attribute name is missing
            print("** attribute name missing **")
            return
        if len(args) == 1:  # instance id is missing
            print("** instance id missing **")
            return
        storage.reload()
        instances = storage.all()
        copy_instances = instances.copy()
        for key, instance in copy_instances.items():
            # checks if the key contains the requested id
            if re.search(f".*{'.'}{args[1]}$", key):
                # Removing the quotation marks of attribute
                # value as it causes errors
                val = args[3].strip('\"')
                # casting the value to attribute type
                type_attr = type(args[2])
                instances[key][args[2]] = type_attr(val)
                storage.save()
                return

    def do_quit(self, argv):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, argv):
        """End of File, exits command interpreter"""

        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
