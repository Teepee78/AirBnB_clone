#!/usr/bin/env python3
"""Entry point of the command interpreter"""
import cmd
import json
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
                inst = BaseModel(**instance)
                print(inst)
                return
        print("** no instance found **")

    def do_quit(self, argv):
        """Quits command interpreter"""

        return True

    def do_EOF(self, argv):
        """End of File, exits command interpreter"""

        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
