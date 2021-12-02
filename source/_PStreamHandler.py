
from . import _defaults as DEFAULTS

import logging


class PStreamHandler:

	def __init__(self,**kwargs):

		if 'format' in kwargs:
			format = kwargs['foramt']
		else:
			format = DEFAULTS.PLOG_FORMAT_MSG

		if 'datefmt' in kwargs:
			datefmt = kwargs['datefmt']
		else:
			datefmt = DEFAULTS.PLOG_FORMAT_DATE

		if 'level' in kwargs:

			if kwargs['level'] in DEFAULTS.PLOG_LEVEL_DICT:
				level = DEFAULTS.PLOG_LEVEL_DICT[kwargs['level']]
			elif isinstance(kwargs['level'],int):
				level = kwargs['level']
			else:
				raise Exception('WrongLevelInput')
		else:
			level = DEFAULTS.PLOG_INFO_NO

		
		logFormatter = logging.Formatter(format,datefmt)
		self.streamHandler = logging.StreamHandler()
		self.streamHandler.setFormatter(logFormatter)
		self.streamHandler.setLevel(level)

	def GetStreamHandler(self):
		return self.streamHandler