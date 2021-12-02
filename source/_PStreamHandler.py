from . import _defaults as DEFAULTS
from ._PFilter import PFilter

import logging


class PStreamHandler:

	def __init__(self,**kwargs):

		# get valid parameters
		filename, format, datefmt, level,filter = DEFAULTS.CheckParameters(**kwargs)

		logFormatter = logging.Formatter(format,datefmt)
		self.streamHandler = logging.StreamHandler()
		self.streamHandler.setFormatter(logFormatter)
		self.streamHandler.setLevel(level)

		# set filter
		filterObject = PFilter(filter)
		self.streamHandler.addFilter(filterObject)

	def GetStreamHandler(self):
		return self.streamHandler