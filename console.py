#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import json
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex


# List of classes
classes = [
    "BaseModel",
    "User",
    "Place",
    "State",
    "City",
    "Amenity",
    "Review"
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
    args = shlex.split(argv, posix=False)
    # Check if class exists
    if args[0] not in classes:
        print("** class doesn't exist **")
        return
    return args


def parse_default(argv):
    """Removes empty strings from arguments
    removes function name

    Args:
        argv: list - arguments

    Return:
        returns argument strings
    """
    # Remove function name
    argv.pop(1)
    # remove empty strings
    for i in argv:
        try:
            argv.remove('')
        except ValueError:
            break
    return " ".join(argv)  # convert to string and return


class HBNBCommand(cmd.Cmd):
    """Contains functions for command interpreter"""
    prompt = "(hbnb) "

    def do_create(self, argv):
        """
        Creates a new instance of a class,
        saves it to JSON file and prints ID

        Usage: create <class name>
        """

        args = parser(argv)
        if args is None:
            return
        instance = eval(f"{args[0]}()")
        # save to json file
        storage.save()
        print(instance.id)

    def do_show(self, argv):
        """
        Prints the string representation of an instance based on the
        class name and id

        Usage: show <class name> <id>
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
        try:
            id_only = args[1].strip('\"').strip("'")
        except ValueError:
            pass
        # Search instances
        for key, instance in instances.items():
            search = f"{args[0]}.{id_only}"
            if search == key:
                print(instance)
                return
        print("** no instance found **")

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id

        Usage: destroy <class name> <id>
        """
        args = parser(argv)
        if args is None:
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage.reload()
        instances = storage.all()
        try:
            id_only = args[1].strip('\"').strip("'")
        except ValueError:
            pass
        for key, instance in instances.items():
            search = f"{args[0]}.{id_only}"
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

        Usage: all or all <class name>
        """
        inst_str_list = []

        # Case 1: Argument is not provided
        if len(argv) == 0:
            storage.reload()
            instances = storage.all()
            for key, instance in instances.items():
                # append string representation to list
                inst_str_list.append(instance.__str__())
            print(inst_str_list)
            return

        args = argv.split()
        # Check if classes exists
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        # Case 2: Argument is provided
        storage.reload()
        instances = storage.all()
        for key, instance in instances.items():
            # Checks if the key contains the name of the class
            if re.search(f"{args[0]}{'.'}.*", key):
                # Append instance to list
                inst_str_list.append(instance.__str__())
        print(inst_str_list)

    def do_update(self, argv):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute

        Usage: update <class name> <id> <attribute> <value>
        """
        args = parser(argv)
        if args is None:
            return
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
            # Removing qoutation mark from id if present
            try:
                id_only = args[1].strip('\"').strip("'")
            except ValueError:
                pass
            # checks if the key contains the requested id
            if re.search(f".*{'.'}{id_only}$", key):
                # Removing the quotation marks of attribute
                # value as it causes errors
                val = args[3].strip('\"').strip("'")
                # casting the value to attribute type
                try:
                    val = int(val)  # cast to integer
                except ValueError:
                    try:
                        val = float(val)
                    except ValueError:
                        pass
                # Update the attribute of the instance
                setattr(instances[key], args[2], val)
                storage.save()
                return
        print("** no instance found **")

    def emptyline(self):
        """Called when an empty line is entered"""
        # This function is overriden so that the
        # last command is not executed when an
        # empty line is entered
        pass

    def do_quit(self, argv):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, argv):
        """End of File, exits command interpreter"""

        print()
        return True

    def all(self, argv):
        """Handles the all command for the default method"""

        # Parse argument
        args = parse_default(argv)
        # Call do_all method
        self.do_all(args)

    def count(self, argv):
        """Handles the count command for the default method"""

        # Parse argument
        args = parse_default(argv)

        # count instances
        inst_str_list = []
        storage.reload()
        instances = storage.all()
        for key, instance in instances.items():
            # Checks if the key contains the name of the class
            if args in key:
                # Append instance to list
                inst_str_list.append(instance)
        print(len(inst_str_list))

    def show(self, argv):
        """Handles the show command for the default method"""
        # Parse argument
        args = parse_default(argv)
        # call show method
        self.do_show(args)

    def destroy(self, argv):
        """Handles the destroy command for the default method"""

        # Parse argument
        args = parse_default(argv)
        # call destroy method
        self.do_destroy(args)

    def update(self, argv):
        """Handles the update command for the default method"""
        argv_copy = argv.copy()
        if re.search(r"{.*}", argv_copy[2]):
            # Dictionary
            new_argv = []
            found_dict = re.search(r"{.*}", argv_copy[2]).group(0)
            try:
                found_id = re.search(".{8}-.{4}-.{4}-.{4}-.{12}",
                                     argv_copy[2]).group(0)
            except AttributeError:
                print("** no instance found **")
                return
            found_dict = found_dict.replace("'", '"')
            actual_dict = json.loads(found_dict)
            # checking if the id exists
            insts = storage.all()
            found = 0
            for key, value in insts.items():
                if re.search(f".*{'.'}{found_id}$", key):
                    found = 1

            if found == 0:
                print("** no instance found **")
                return

            for key, value in actual_dict.items():
                new_argv = []
                new_argv.append(argv_copy[0])
                new_argv.append(argv_copy[1])
                new_argv.append(found_id)
                new_argv.append(key)
                new_argv.append(str(f'"{value}"'))
                args = parse_default(new_argv)
                copy_args = args
                if parser(copy_args) is None:
                    return
                self.do_update(args)
        else:
            # Not a dictionary
            # Parse argument
            args = parse_default(argv)
            # remove comma
            args = args.replace(',', '')
            # call update method
            self.do_update(args)

    def default(self, argv):
        """Handles commands that doesn't exist"""

        # List of commands
        commands = ["all", "count", "show", "destroy", "update"]
        # Split arguments by dot and parentheses
        args = re.split(r'[\(\).]', argv)
        # Check if first argument is in classes
        if args[0] in classes:
            # Check for second argument
            if args[1] in commands:
                eval_string = f"self.{args[1]}({args})"
                eval(eval_string)
            else:
                print(f"*** Unknown syntax: {'.'.join(args)}")
        else:  # Print error message
            print(f"*** Unknown syntax: {'.'.join(args)}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
