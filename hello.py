""""
Author: James Fehr
Mostly a repeat of a previous script, but with a few changes.
This is a simple Python script that greets the user by name.
"""
import sys

def hello(args):    # define a function called hello
    for name in args:    # loop through the names in args
        print("Hello,", name)   # print the names in args

if __name__ == "__main__":  # If this script is run from the command line
    arguments = sys.argv[1:]  # Exclude the script name itself
    hello(arguments)    # Call the hello function with the arguments
