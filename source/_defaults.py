
# format and color value
PLOG_HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


BLACK = '\033[30m'
RED = '\033[31m' 
GREEN = '\033[32m' 
YELLOW = '\033[33m' 
MAGENTA = '\033[35m' 
WHITE = '\033[37m' 

# format
PLOG_FORMAT_MSG = '[%(asctime)s ]%(_module)-12s|%(levelname)-8s| %(message)s'
PLOG_FORMAT_DATE = '%Y-%m-%d %H:%M:%S'


# level
PLOG_CRITICAL_NO = 50 # 50
PLOG_CRITICAL_ICON = u'\U0001F480'

PLOG_ERROR_NO = 40 # 40
PLOG_ERROR_ICON = u'\U0001274C'

PLOG_WARNING_NO = 30 # 30
PLOG_WARNING_ICON = u'\U000026A0'


PLOG_INFO_NO = 20 # 20
PLOG_INFO_ICON = u'\U00002139'

PLOG_DEBUG_NO = 10 # 10
PLOG_DEBUG_ICON = u'\U0001F41E'

PLOG_NOTSET_NO = 0 #0
PLOG_NOTSET_ICON = u'\U0001F47D'

PLOG_LEVEL_DICT = {'critical':PLOG_CRITICAL_NO, 'error': PLOG_ERROR_NO, 'warning':PLOG_WARNING_NO, 'info':PLOG_INFO_NO,'debug':PLOG_DEBUG_NO ,'none':PLOG_NOTSET_NO}

# unit
PLOG_UNIT_SIZE = ['B','KB','MB','GB']
PLOG_UNIT_TIME = ['SECOND','MINUTE','HOUR','DAY','WEEK',':']


