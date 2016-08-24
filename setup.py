#!/usr/bin/env python3

import os
from setuptools import setup
from cpm import __projname__, __projver__, __projdesc__


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
#
# list of classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    name = __projname__,
    version = __projver__,
    author = "Benjamin Boortz",
    author_email = "benjamin.boortz@secure.mailbox.org",
    description = (__projdesc__),
    license = "GPLv3",
    keywords = "container package manager",
    url = "http://packages.python.org/cpm",
    packages=['cpm', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
    ],
    test_suite = "cpm.tests.test_all",
)
