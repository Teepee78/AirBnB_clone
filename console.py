#!/usr/bin/env python3
"""Entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains functions for command interpreter"""


    prompt = "(hbnb) "

    def do_quit(self, argv):
        """Quits command interpreter"""

        return True

    def do_EOF(self, argv):
        """End of File, exits command interpreter"""

        print()
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
