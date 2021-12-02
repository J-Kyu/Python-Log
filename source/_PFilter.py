import logging

class PFilter(logging.Filter):

	def __init__(self, func):
		self.func = func

	def filter(self,record):
		return self.func(record)


