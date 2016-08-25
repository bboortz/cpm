from cpm.logger import getLogger
from cpm.json import jsonUtil
from cpm.process import process

LOGGER = getLogger('run')


class run(object):

    def __init__(self):
        self.jsonUtil = jsonUtil()

    def run(self, config_file="cp.json"):
        """build the container package.
        """

        LOGGER.debug("RUN")
        json_data = self.jsonUtil.readJson(config_file)
        self.jsonUtil.printJson(json_data['cpJson'])
        command = json_data['cpJson']['cpJsonBody']['run']['runCommand']
        LOGGER.debug(command)
        cmd_arr = command.split()
        p = process()
        p.execute(cmd_arr, shell=True)
        

