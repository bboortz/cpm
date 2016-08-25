from cpm.logger import getLogger
from cpm.json import jsonUtil
from cpm.process import process

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
        command = json_data['cpJson']['cpJsonBody']['build']['buildCommand']
        LOGGER.debug(command)
        cmd_arr = command.split()
        p = process()
        p.execute(cmd_arr, directory)
        

