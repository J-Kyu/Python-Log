from ._PAbsFileHandler import PAbsFileHandler
import logging.handlers
import datetime


class PTimedFileHandler(PAbsFileHandler):

    def __init__(self, filename, timeRotation = None, backupCount = 10):

        '''
        timeRotation Unit Example
        12:00
        10 days
        1 week
        '''

        when = 'h'
        interval = 1
        encoding = None
        delay = False
        utc = False
        atTime = None
        errors = None

        # set atTime 
        if ':' in timeRotation:

            # parsing
            atTimeList = timeRotation.split(':')
            when = 'midnight'
            # hour:minutes
            if len(atTimeList) == 2:
                atTime = datetime.time(int(atTimeList[0]),int(atTimeList[1]), 00)
            # hour:minutes:seconds
            elif len(atTimeList) == 3:
                atTime = datetime.time(int(atTimeList[0]),int(atTimeList[1]), int(atTimeList[2]))
            else:
                raise Exception("Wrong Format for time: {}".format(timeRotation))
    
        # Interval
        elif 'SECOND' in timeRotation.upper() or 'SECONDS' in timeRotation.upper():
            # seconds
            when  = 'S'
            unitIndex = timeRotation.upper().find('SECOND')
            interval = int(timeRotation[:unitIndex])
            

        elif 'MINUTE' in timeRotation.upper() or 'MINUTES' in timeRotation.upper():
            # minute
            when  = 'M'
            unitIndex = timeRotation.upper().find('MINUTE')
            interval = int(timeRotation[:unitIndex])
            

        elif 'HOUR' in timeRotation.upper() or 'HOURS' in timeRotation.upper():
            # hour
            when  = 'H'
            unitIndex = timeRotation.upper().find('HOUR')
            interval = int(timeRotation[:unitIndex])
            

        elif 'DAY' in timeRotation.upper() or 'DAYS' in timeRotation.upper():
            # day
            unitIndex = timeRotation.upper().find('DAY')

            # n days
            if timeRotation[:unitIndex].isdigit() == True:
                when = 'D'
                interval = int(timeRotation[:unitIndex])

            
            # monday ~ sunday
            else:

                if 'SUNDAY' in timeRotation.upper():
                    # sunday
                    when = 'W6'

                elif 'MONDAY' in timeRotation.upper():
                    # monday
                    when = 'W0'

                elif 'TUESDAY' in timeRotation.upper():
                    # tuesday
                    when = 'W1'

                elif 'WEDNESDAY' in timeRotation.upper():
                    # wednesday
                    when = 'W2'

                elif 'THURSDAY' in timeRotation.upper():
                    # thursday
                    when = 'W3'

                elif 'FRIDAY' in timeRotation.upper():
                    # friday
                    when = 'W4'

                elif 'SATURDAY' in timeRotation.upper():
                    # saturday
                    when = 'W5'

                else:
                    raise Exception('Wrong Input for day; {}'.format(timeRotation))


        elif 'WEEK' in timeRotation.upper() or 'WEEKS' in timeRotation.upper():
            # 7 days * each  week

                when = 'D'
                unitIndex = timeRotation.upper().find('WEEK')
                interval = int(timeRotation[:unitIndex]) * 7


        else:
            raise Exception('Wrong Input: {}'.format(timeRotation))

        self.fileHandler = logging.handlers.TimedRotatingFileHandler(filename, when = when, interval=interval, backupCount=backupCount, atTime=atTime)
