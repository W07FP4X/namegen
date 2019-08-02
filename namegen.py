#!/usr/local/bin/python3

"""namegen.py - a unique name generator service."""
from base64 import b32encode
from os import urandom
import random
import os


def read_file(filename):
    """A method for reading file contents.

        Parameters
        ----------
        filename : str
            The filename to read.
    """
    try:
        filehandle = open(filename)
        file_data = filehandle.read()
        filehandle.close()
        return file_data
    except OSError as err:
        print("Error reading file: {0}".format(err))


class NameGenerator():
    """A class used to generate unique names.

    ...

    Methods
    -------
    generate_names(count)
        Generates unique names in human and machine readable format.
    """

    def generate_names(self, count=1):
        """A method for generating unique names.

        If the argument `count` isn't passed in, the default count of 1 is used.

        Parameters
        ----------
        count : str
            The count of unique names to generate
        """
        unique_names = []
        #absolute dir of the name data
        script_dir = os.path.dirname(__file__)
        rel_path = "data/names.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        try:
            name_list = read_file(abs_file_path).split()
        except ValueError:
            print("Error parsing names.txt file contents.")
        for i in range(count):
            key = b32encode(urandom(5))
            #concat names and UTF-8 key
            unique_name = name_list[random.randint(0, len(name_list) - 1)] + '_' + name_list[random.randint(0, len(name_list) - 1)] + '_' + key.decode('UTF-8')
            unique_names.append(unique_name)
        return unique_names
