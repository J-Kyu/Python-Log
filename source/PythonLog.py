from . import _defaults as DEFAULTS
from ._PFileHandler import PFileHandler
from ._PStreamHandler import PStreamHandler

import inspect 
import datetime
import logging.handlers
import os
import sys

class PythonLog:
    def __init__(self):
        self.logPath = os.path.dirname(__file__)+"/.."

        # set default root logger
        logging.basicConfig(level=logging.DEBUG,
                    format=DEFAULTS.PLOG_FORMAT_MSG,
                    datefmt=DEFAULTS.PLOG_FORMAT_DATE)
 
        # get root  logger 
        self.logger = logging.getLogger('') # name of logger

        # add null handler 
        self.__AddNullHandler()

        # remove default stream handler
        # For now, only null handler is handling logger (stream or file handler should be added)
        self.logger.removeHandler(self.logger.handlers[0])

    def temp(self):
        #print(logging.getLogger().handlers)
        print(self.logger.handlers)

    def addStreamHandler(self, **kwargs):
        '''
        Default root logger Setting

        this method will check parameters and set valid variable for logger
        Default Stream Handler will be added
        '''
        # set stream handler
        pStreamHandler = PStreamHandler(**kwargs)
        self.logger.addHandler(pStreamHandler.GetStreamHandler())


    def addFileHandler(self,**kwargs): 
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

        '''
        # set file handler
        pFileHandler = PFileHandler(**kwargs)
        self.logger.addHandler(pFileHandler.GetFileHandler())

      


    def __AddNullHandler(self):
        '''
        Default Handler
        '''
        self.logger.addHandler(logging.NullHandler())




    '''
    extra(d) are all related to filter.....
    i got to redo it in the future
    '''

 
    def critical(self,log):
        d = { '_module' : self.__GetCalleeModule()}
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

