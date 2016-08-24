#!/usr/bin/env python3

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
#
# list of classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cpm",
    version = "0.0.1",
    author = "Benjamin Boortz",
    author_email = "benjamin.boortz@secure.mailbox.org",
    description = ("A package manager for container"),
    license = "GPLv3",
    keywords = "container package manager",
    url = "http://packages.python.org/cpm",
    packages=['src', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
