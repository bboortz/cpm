#!/usr/bin/env python3


import os
import sys
import argparse
from cpm import __projname__, __projver__, __projdesc__
from cpm.logger import getLogger
from cpm.cmd.build import build
from cpm.cmd.install import install
from cpm.cmd.run import run

try:
    # For Python 3.0 and later
    from setuptools_scm import get_version
    scm_version = " (%s)" % get_version()
    FileNotFoundError
except ImportError:
    scm_version = ""
    FileNotFoundError = IOError



#
# * basic configuration *
#
LOGGER = getLogger('cpm')


#
# * parse arguments *
#


# define the parser arguments
parser = argparse.ArgumentParser(prog=__projname__, description=__projdesc__)
#from _version import __version__
parser.add_argument('-V', '--version', action='version', version='%(prog)s {version}{scm_version}'.format(version=__projver__, scm_version=scm_version))
subparsers = parser.add_subparsers(dest="subparser_name") # this line changed
build_parser = subparsers.add_parser('build', help='build a package')
build_parser.add_argument('-c', '--config-file', dest='config_file', help='specify the config file')
build_parser.add_argument('-d', '--directory', dest='directory', help='specify the image directory')
install_parser = subparsers.add_parser('install', help='install a package')
install_parser.add_argument('CONTAINER', help='the container to install')
run_parser = subparsers.add_parser('run', help='run the container')
run_parser.add_argument('CONTAINER', help='the container to run')


# parse the arguments
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

args = vars( parser.parse_args() )
LOGGER.debug(args)

if 'subparser_name' not in args:
    parser.print_help()
    sys.exit(1)

subparser_name = args['subparser_name']


def retrieveArgument(args, arg_name):
    if arg_name in args:
        return args[arg_name]
    else:
        return None



# parse the subparser / commands
if subparser_name == 'build':
    try:
        config_file = retrieveArgument(args, "config_file")
        cmd = build()
        cmd.build(config_file=config_file)
    except FileNotFoundError as fnfe:
        LOGGER.error(fnfe)
    except ValueError as ve:
        LOGGER.error("error while parsin json file: %s" % ve)
elif subparser_name == 'install':
    container_name = args['CONTAINER']
    cmd = install()
    cmd.install(container_name)
elif subparser_name == 'run':
    container_name = args['CONTAINER']
    cmd = run()
    cmd.run(container_name)
else:
    parser.print_help()
    sys.exit(1)

