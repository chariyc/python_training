# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK


def hello():
    """Print "Hello World" and return None."""
    print("Hello World")


def bye():
    """Print "Good Bye World" and return None."""
    print("Good Bye World")


# Main program starts here
hello()
bye()

mylongvariablename = 42
myshortvariablename = 43
print("myshortvariablename is = ", myshortvariablename)
print("mylongvariablename is = ", mylongvariablename)
mylongvariablename += 100
myshortvariablename += 100
print("myshortvariablename is = ", myshortvariablename)
print("mylongvariablename is = ", mylongvariablename)

# This is a sample comment line (ctrl-1)

# =============================================================================
# This is a sample comment block (ctrl-4)
# =============================================================================

"""A file which is a module."""


def func():
    """
    Yowza.

    This is a sample docstring
    """
    pass


def func1():
    """Oh yeah."""


def func2():
    """Youch."""
    pass
