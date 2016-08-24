#!/usr/bin/env python3

import os
import sys
import argparse
from cpm import __projname__, __projver__, __projdesc__
from cpm.cmd.build import build
from cpm.cmd.install import install
from cpm.cmd.run import run


#
# * parse arguments *
#


# define the parser arguments
parser = argparse.ArgumentParser(prog=__projname__, description=__projdesc__)
#from _version import __version__
parser.add_argument('-V', '--version', action='version', version='%(prog)s {version}'.format(version=__projver__))
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
#print(args)

if 'subparser_name' not in args:
    parser.print_help()
    sys.exit(1)

subparser_name = args['subparser_name']


# parse the subparser / commands
if subparser_name == 'build':
    cmd = build()
    cmd.build()
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

