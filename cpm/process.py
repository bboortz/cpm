import sys
from cpm.logger import getLogger
from cpm.nbstreamreader import NonBlockingStreamReader as NBSR
from subprocess import Popen, PIPE
from time import sleep



LOGGER = getLogger('build')



class process(object):

    def __init__(self):
        pass

    def execute(self, cmd_arr, directory='.', shell=False):
        LOGGER.debug("execute command: %s" % ' '.join(cmd_arr) )
        proc = Popen(cmd_arr, cwd=directory, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=shell)
        # wrap p.stdout with a NonBlockingStreamReader object:
        nbsr = NBSR(proc.stdout)
        # get the output
        while True:
            output = nbsr.readline(0.1)
            # 0.1 secs to let the shell output the result
            if not output:
                LOGGER.debug("command executed. end of data" )
                break
            LOGGER.info( output.decode('utf-8').strip() )
