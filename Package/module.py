# this is a file, otherwise known as a "module" in python

# the __future__ module can help make in built functions backwards compatible
# https://docs.python.org/2/library/__future__.html
from __future__ import print_function
import os
from sys import platform
import json


def function():
    # get the path to this module (file)
    file_path = os.path.dirname(os.path.abspath(__file__))
    # determine what slash is used for this file system
    slash = syscheck()
    file_path_split = file_path.split(slash)
    module_name = file_path_split[-1]
    package_name = file_path_split[-2]
    print("Inside of file: {} \nInside the package: {}".format(module_name, package_name))
    read_file(file_path, slash)


def read_file(path, slash):
    # access the .json file, even AFTER its been pip installed (see MANIFEST.in)
    with open(path + slash + 'file.json', 'r') as myfile:
        data = myfile.read()
    parsed_data = json.loads(data)
    print('accessing the dictionary stored in the .json-> key:{}'.format(parsed_data['key']))


def syscheck():
    """
    Jack C. Cook
    Saturday, February 15, 2020

    Check the operating system to determine what slash is used

    :return: the "slash" that is used on the OS
    """
    if "darwin" in platform or "linux" in platform:
        slash = r'/'
    elif platform == "win32" or platform == "win64":
        slash = '\\'
    else:
        raise ValueError("The platform: {} is not currently handled by this function.".format(platform))
    return slash
