from cpm.logger import getLogger
from cpm.json import jsonUtil

LOGGER = getLogger('build')


class build(object):

    def __init__(self):
        self.jsonUtil = jsonUtil()

    def build(self, directory=".", config_file="cp.json"):
        """build the container package.
        """

        LOGGER.debug("BUILD")
        json_data = self.jsonUtil.readJson(config_file)
        self.jsonUtil.printJson(json_data['cpJson'])
        buildCommand = json_data['cpJson']['cpJsonBody']['build']['buildCommand']
        LOGGER.debug(buildCommand)
        

