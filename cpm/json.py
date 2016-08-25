import json
from pprint import pprint


class jsonUtil(object):

    def __init__(self):
        pass

    def readJson(self, file):

        with open(file) as data_file:
                json_data = json.load(data_file)

        return json_data


    def printJson(self, json_data):
        pprint(json_data)


