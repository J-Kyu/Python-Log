from ._PAbsFileHandler import PAbsFileHandler
import logging.handlers


class PRotatingFileHandler(PAbsFileHandler):

    def __init__(self, filename, mode = 'a', maxBytesWithUnit= '1 MB', backupCount=10, encoding=None, delay=False, errors=None):
        maxBytes = 0

                # Kilo Byte
        if 'KB' in maxBytesWithUnit:
            unitIndex = maxBytesWithUnit.upper().find('KB')
            maxBytes = int(maxBytesWithUnit[:unitIndex]) * 10**3
        # Mega byte
        elif 'MB' in maxBytesWithUnit:
            unitIndex = maxBytesWithUnit.upper().find('MB')
            maxBytes = int(maxBytesWithUnit[:unitIndex]) * 10**6
        # Giga byte
        elif 'GB' in maxBytesWithUnit:
            unitIndex = maxBytesWithUnit.upper().find('GB')
            maxBytes = int(maxBytesWithUnit[:unitIndex]) * 10**9

        elif 'B' in maxBytesWithUnit:
            unitIndex = maxBytesWithUnit.upper().find('B')
            maxBytes = int(maxBytesWithUnit[:unitIndex]) * 10**0

        elif maxBytesWithUnit.isdigit() == True:
            maxBytes = int(maxBytesWithUnit) 

        else:
            raise Exception("Given maxBytesWithUnit is neigther in int nor with right format of Unit. Please check a gain ")

        

        self.fileHandler = logging.handlers.RotatingFileHandler(filename, mode=mode, maxBytes=maxBytes, backupCount=backupCount)
