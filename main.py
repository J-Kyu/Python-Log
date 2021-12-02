from source import logger
import time

logger.temp()
def temp(record):
	record.msg += "---{}".format(record.lineno)
	return True


logger.addStreamHandler(level = 'info', filter = temp)
logger.addStreamHandler(level = 'error')
logger.addFileHandler(filename = 'log.log', level = 'info')
logger.addFileHandler(filename = 'error.log', level = 'error')
i = 0 

#logger.addStreamHandler(level = 'debug')
logger.info("This is info")
'''
logger.debug("THIS is DEBUG")
logger.warning("THIS is warning")
logger.error("THIS is error")
'''
logger.critical("This is critical")
