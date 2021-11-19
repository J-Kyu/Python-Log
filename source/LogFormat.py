import os
import logging
import sys
import datetime


logCount = 0
logNumb = 0
LOG_TITLE = '{0}-{1}-{2}.log'.format('GSMS',str(datetime.date.today()),logNumb)
LOG_PATH = os.path.dirname(__file__)+"/.."

FULL_PATH = '{0}/{1}'.format(LOG_PATH,LOG_TITLE)
if not os.path.exists(FULL_PATH):
    f = open(FULL_PATH,'w')
    f.close()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(FULL_PATH)
formatter = logging.Formatter('[%(asctime)s %(module)s %(levelname)s]%(message)s', '%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class LogFormat:

   
    HEADER = '\033[95m'
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

    @staticmethod
    def Print(str):
        print("{}".format(str))

    @staticmethod
    def Warning(str):
        print(LogFormat.WARNING+"{}".format(str)+LogFormat.ENDC)

    @staticmethod
    def Error(str):
        print(LogFormat.FAIL+"{}".format(str)+LogFormat.ENDC)


    @staticmethod
    def Good(str):
        print(LogFormat.OKGREEN+"{}".format(str)+LogFormat.ENDC)

    @staticmethod
    def ColorBlue(str):
        print(LogFormat.OKBLUE+"{}".format(str)+LogFormat.ENDC)

    @staticmethod
    def ColorCyan(str):
        print(LogFormat.OKCYAN+"{}".format(str)+LogFormat.ENDC)
    
    @staticmethod
    def PIDLog(str, subTitle = "", code = 1):
        '''
        code 1: Print
        code 2: Warning
        code 3: Error
        code 4: Good
        code 5: ColorBlue
        code 6: ColorCyan
        default: Print
        '''

        pid = os.getpid()
        str = "[PID: {} | {}] - {}".format(pid,subTitle,str)

        if code == 1:
            LogFormat.Print(str)
            logging.debug(str)
        elif code == 2:
            LogFormat.Warning(str)
        elif code == 3:
            LogFormat.Error(str)
        elif code == 4:
            LogFormat.Good(str)
        elif code == 5:
            LogFormat.ColorBlue(str)
        elif code == 6:
            LogFormat.ColorCyan(str)
        else:
            LogFormat.Print(str)


    @staticmethod
    def GSMSMonitorThumbnail(version):
        print("   ___________ __  ________    __  ___            _ __            ")
        print("  / ____/ ___//  |/  / ___/   /  |/  /___  ____  (_) /_____  _____")
        print(" / / __ \__ \/ /|_/ /\__ \   / /|_/ / __ \/ __ \/ / __/ __ \/ ___/")
        print("/ /_/ /___/ / /  / /___/ /  / /  / / /_/ / / / / / /_/ /_/ / /    ")
        print("\____//____/_/  /_//____/  /_/  /_/\____/_/ /_/_/\__/\____/_/ ")
        print(version)

    @staticmethod
    def GSSBookLog(book):

        print("|{: ^5}|{: ^16}|{: ^32}|{: ^16}|{:^16}|{: ^16}|{: ^16}|".format("#","Title","Token","PID","IP","PORT","IsAlive"))
        print("{:─^125}".format(""))
        for i,(key,val) in enumerate(book.items()):
            print("|{:^5}|{: ^16}|{: ^32}|{: ^16}|{: ^16}|{: ^16}|{: ^16}|".format(i,val.title,key,val.pid,val.ip,val.port,val.isAlive))
    
    @staticmethod
    def ChangeLogger():
        
        global logCount
        global logNumb

        logNumb += 1
        logCount = 0
        #remove logger
        logger.handlers[0].stream.close()
        logger.removeHandler(logger.handlers[0])

        # renew name
        LOG_TITLE = '{0}-{1}-{2}.log'.format('GSMS',str(datetime.date.today()),logNumb)
 
        FULL_PATH = '{0}/{1}'.format(LOG_PATH,LOG_TITLE)
        if not os.path.exists(FULL_PATH):
            f = open(FULL_PATH,'w')
            f.close()

        # set logger
        file_handler = logging.FileHandler(FULL_PATH)
        formatter = logging.Formatter('[%(asctime)s %(module)s %(levelname)s]%(message)s', '%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


    @staticmethod
    def RequestLog(req,ip='',port=''):
         
        global logCount
        global logNumb

        # write request log
        logCount += 1
        log = "[Requesting From {0}:{1}]-{2}".format(ip,port,req)
        #logger.info(log)

        # change logger
        if logCount > 100:
            LogFormat.ChangeLogger()
    @staticmethod
    def ResponseLog(res,ip='',port=''):

        global logCount
        global logNumb

       # write response log
        logCount += 1
        log = "[Response To  {0}:{1}]-{2}".format(ip,port,res)
        #logger.info(log)

        # change logger
        if logCount > 100:
            LogFormat.ChangeLogger()


