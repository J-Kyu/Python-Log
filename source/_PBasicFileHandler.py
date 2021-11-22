import logging
from ._PAbsFileHandler import PAbsFileHandler
from . import _defaults as DEFAUTLS


class PBasicFileHandler(PAbsFileHandler):


    def __init__(self, fileName, mode = 'a', encoding = None, delay= False, errors = None, **kwargs ):
        self.fileHandler = logging.FileHandler(fileName)
        #self.basicFileHandler = logging.FileHandler(fileName)

    def GetFileHandler(self):
        return self.fileHandler
