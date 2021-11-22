from source import logger
import time

logger.add(fileName = "./log/test.log",rotation = '200 B')
#logger.add(fileName = "test.log")

while True:
    time.sleep(1)

    logger.info("This is info")


logger.info("This is info")
logger.debug("THIS is DEBUG")
logger.warning("THIS is warning")
logger.error("THIS is error")
logger.critical("This is critical")
