#!/usr/bin/python3
"""
    a simple, testable, routine inspired by Hello World

This is a simple script wrapped around a simple routine written with a view to
  - checking that python, pydoc, unittest and pylint are installed properly;
  - providing a simple starting point for writing other scripts in python.

"""

__author__ = """New Forester <NewForester@users.noreply.github.com>
MIT Licence @ https://opensource.org/licenses/MIT"""

import sys

def greet (who):
    """
    Greet someone or something

    Parameters - who (string) - who or what to greet

    Return - (string) - greeting
    """
    return "Hello {0}".format(who)

# ------------------------------

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Greet everyone on the command line

        for arg in sys.argv[1:]:
            print(greet(arg))
    else:
        # Greet the entire world

        print(greet("World"))

# EOF
