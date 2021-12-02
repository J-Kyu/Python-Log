from ._PRotatingFileHandler import PRotatingFileHandler
from ._PTimedFileHandler import PTimedFileHandler
from ._PBasicFileHandler import PBasicFileHandler

from . import _defaults as DEFAULTS

import logging


class PFileHandler:

    def __init__(self, **kwargs ):

        self.fileHandler = None

        # filename
        if 'filename' in kwargs:
            filename = kwargs['filename']
        else:
            filename = 'log.log'


        # set format of logger
        if 'format' in kwargs:
            format = kwargs['format']
        else:
            format = DEFAULTS.PLOG_FORMAT_MSG

        if 'datefmt' in kwargs:
            datefmt = kwargs['datefmt']
        else:
            datefmt = DEFAULTS.PLOG_FORMAT_DATE

        # level
        if 'level' in kwargs:

            if kwargs['level'] in DEFAULTS.PLOG_LEVEL_DICT:
                level = DEFAULTS.PLOG_LEVEL_DICT[kwargs['level']]
            elif isinstance(kwargs['level'],int):
                level = kwargs['level']
            else:
                raise Exception('WrongLevelInput')

        # check if filehandler require rotation option
        if 'rotation' in kwargs:
            # size
            if self._IsSharingAnyElement(DEFAULTS.PLOG_UNIT_SIZE, kwargs['rotation']):
                self.fileHandler = PRotatingFileHandler(filename = filename, maxBytesWithUnit = kwargs['rotation'])
            # time
            elif self._IsSharingAnyElement(DEFAULTS.PLOG_UNIT_TIME, kwargs['rotation']):
                self.fileHandler = PTimedFileHandler(filename = filename, timeRotation = kwargs['rotation'])
            else:
                raise Exception("Unavailble Unit: {}".format(kwargs['rotation']))
    
        # simple file handler
        else:
            self.fileHandler = PBasicFileHandler(filename)

        # set formmater
        logFormatter = logging.Formatter(format,datefmt)
        self.fileHandler.GetFileHandler().setFormatter(logFormatter)

        # set level
        self.fileHandler.GetFileHandler().setLevel(level)
        

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
