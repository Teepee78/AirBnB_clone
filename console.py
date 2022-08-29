#!/usr/bin/env python3
"""Entry point of the command interpreter"""
import cmd
import json
from models.base_model import BaseModel


# List of classes
classes = [
    "BaseModel"
]


class HBNBCommand(cmd.Cmd):
    """Contains functions for command interpreter"""


    prompt = "(hbnb) "

    def do_create(self, argv):
        """Creates a new instance of a class, saves it to JSON file and prints ID"""

        if len(argv) == 0:
            print("** class name missing **")
            return
        # Split argv into a list of strings
        args = argv.split()
        # Check if class exists
        if args[0] not in classes:
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            # save to json file
            with open("models/engine/instances.json", mode="r+", encoding="utf-8") as f:
                if len(f.read()) != 0:
                    f.write("\n")
                f.write(json.dumps(instance.to_dict()))
            print(instance.id)

    def do_quit(self, argv):
        """Quits command interpreter"""

        return True

    def do_EOF(self, argv):
        """End of File, exits command interpreter"""

        print()
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
