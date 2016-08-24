#!/usr/bin/env python3

from cpm import __projname__, __projdesc__
import argparse
import json

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


progname = "jsoncurl"



class jsoncurl(object):

    def __init__(self):
        pass

    def get_jsonparsed_data(self, url):
        """Receive the content of ``url``, parse it as JSON and return the
           object.
        """

        response = urlopen(url)
        data = response.read().decode()
        #return data
        #return json.dumps(data)
        return json.loads(data)

class jsonprint(object):

    def __init__(self):
        pass

    def uprint(self, json_data, element=None):
        if element == None:
            print(json_data)
        else:
            try:
                print(json_data[element])
            except KeyError:
                print("element <%s> not found in json" % element)

    def pprint(self, json_data, element=None):
        if element == None:
            print( json.dumps(json_data, sort_keys=True, indent=4) )
        else:
            try:
                print( json.dumps(json_data[element], sort_keys=True, indent=4) )
            except KeyError:
                print("element <%s> not found in json" % element)



parser = argparse.ArgumentParser(prog=__projname__, description=__projdesc__)
parser.add_argument('-g', '--global')
subparsers = parser.add_subparsers(dest="subparser_name") # this line changed
build_parser = subparsers.add_parser('build', help='build a package')
build_parser.add_argument('-c', '--config-file', dest='config_file', help='specify the config file')
build_parser.add_argument('-d', '--directory', dest='directory', help='specify the image directory')
install_parser = subparsers.add_parser('install', help='install a package')
install_parser.add_argument('CONTAINER', help='the container to install')
args = vars( parser.parse_args() )


jc = jsoncurl()
jp = jsonprint()



#json_data = jc.get_jsonparsed_data( args['URL'] )
if args['extract_element']:
    jp.pprint(json_data, args['extract_element'] )
else:
    jp.pprint(json_data)

