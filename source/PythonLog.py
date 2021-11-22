from . import _defaults as DEFAULTS
from ._PFileHandler import PFileHandler

import inspect 
import datetime
import logging.handlers
import os


class PythonLog:
    def __init__(self):
        self.logPath = os.path.dirname(__file__)+"/.."

        # set root logger
        logging.basicConfig(level=logging.DEBUG,
                    format=DEFAULTS.PLOG_FORMAT_MSG,
                    datefmt=DEFAULTS.PLOG_FORMAT_DATE)

        # get root  logger 
        self.logger = logging.getLogger() # name of logger

    def add(self,level = DEFAULTS.PLOG_NOTSET_NO , msgFormat = DEFAULTS.PLOG_FORMAT_MSG, dateFormat = DEFAULTS.PLOG_FORMAT_DATE, fileName = None, **kwargs): 
            '''
            Add method  handler to logger
            There are 2 handler:
                1. Stream Handler
                2. File Handler
            This method will give style on the log.


            Configure format, rotation, filter, serilaize backtrace, diagnose, catch of log
            each add will generate cycle of a log

            but for now, we configure format and rotation of logger.

            1. Format and Rotation
            2. Filter and backtrace
            3. Colorized
            4. Catch

            CRITICAL = 50
            ERROR = 40
            WARNING = 30
            INFO = 20
            DEBUG = 10
            NOTSET = 0
            '''
            # set format of logger
            logFormatter = logging.Formatter(msgFormat,dateFormat)

            # set file handler
            if fileName != None:

                # !vioilating SRP
                if 'rotation' in kwargs:
                    # rotating file handler for MB size
                    pFileHandler = PFileHandler(fileName, rotation = kwargs['rotation'])
                    self.logger.addHandler(pFileHandler.GetFileHandler())

                # file handler
                else:
                    pFileHandler = PFileHandler(fileName)
                    self.logger.addHandler(pFileHandler.GetFileHandler())
           
            # set stream handler
            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(logFormatter)
            streamHandler.setLevel(level)
            self.logger.addHandler(streamHandler)


    '''
    extra(d) are all related to filter.....
    i got to redo it in the future
    '''

 
    def critical(self,log):
        d = { '_module' : self.__GetCalleeModule() }
        self.logger.critical(log, extra = d)

    def error(self, log):
        d = { '_module' : self.__GetCalleeModule() }
        self.logger.error(log, extra = d)

    def warning(self, log):
        d = { '_module' : self.__GetCalleeModule() }
        self.logger.warning(log, extra = d)
    
    def info(self, log):
        d = { '_module' : self.__GetCalleeModule() }
        self.logger.info(log, extra = d)

    def debug(self,log):
        d = { '_module' : self.__GetCalleeModule() }
        self.logger.debug(log, extra = d)

    def __GetCalleeModule(self):
        '''
        this method will return callee's module name
        since, it is private method which will be called in this module (self.critical(), self.error().......),
        the stack index is 2 instead of 1.
        '''
        frm = inspect.stack()[2]
        mod = inspect.getmodule(frm[0])
        return mod.__name__ 

