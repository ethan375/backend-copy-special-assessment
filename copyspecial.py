#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Ethan375"


def get_special_paths(dir):
    files_in_dir = os.listdir(dir)
    dict_of_special_files = {}
    for file in files_in_dir:
        if '__' in file:
            abs_path_of_special_file = os.path.abspath(file)
            if dict_of_special_files.get(file):
                raise Exception('there are duplicates of this file: {}'.format(file))
            else:
                dict_of_special_files[file] = abs_path_of_special_file
            print(abs_path_of_special_file)

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('--dir', action="store_true", nargs='+')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    directory = args.dir

    if directory:
        get_special_paths(directory)

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    



if __name__ == "__main__":
    main()
