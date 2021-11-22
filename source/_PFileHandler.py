from ._PRotatingFileHandler import PRotatingFileHandler
from ._PTimedFileHandler import PTimedFileHandler
from ._PBasicFileHandler import PBasicFileHandler
from . import _defaults as DEFAULTS

import logging


class PFileHandler:


    def __init__(self, fileName, msgFormat = DEFAULTS.PLOG_FORMAT_MSG,dateFormat = DEFAULTS.PLOG_FORMAT_DATE ,mode = 'a', encoding = None, delay= False, errors = None, **kwargs ):

        self.fileHandler = None

        if 'rotation' in kwargs:
            # size
            if self._IsSharingAnyElement(DEFAULTS.PLOG_UNIT_SIZE, kwargs['rotation']):
                self.fileHandler = PRotatingFileHandler(fileName,maxBytesWithUnit = kwargs['rotation'])
            # time
            elif self._IsSharingAnyElement(DEFAULTS.PLOG_UNIT_TIME, kwargs['rotation']):
                self.fileHandler = PTimedFileHandler(fileName, timeRotation = kwargs['rotation'])
            else:
                raise Exception("Unavailble Unit: {}".format(kwargs['rotation']))
    
        else:
            # file handler
            self.fileHandler = PBasicFileHandler(fileName)

        logFormatter = logging.Formatter(msgFormat,dateFormat)
        # set formmater
        self.fileHandler.GetFileHandler().setFormatter(logFormatter)
        

    def _IsSharingAnyElement(self, l1,wrd):
        '''
        check if element of list l1 is at  string wrd
        If l1 shares at least one element, return True
        else, return False
        '''
        for i in l1:
            if i in wrd.upper():
                return True
        return False

    def GetFileHandler(self):
        return self.fileHandler.GetFileHandler()
