import os
from datetime import datetime


#Path where the csv is stored on the disk
#Change Accordingly
path = r'/Users/yaaseen/Desktop/gnuradio'
os.chdir(path)

fileName = datetime.now().strftime("%Y.%m.%d-%H:%M:%S") + ".csv"
class TimedValue:
    
    def __init__(self):
        global fileName
        self._started_at = datetime.now()
        fileName = datetime.now().strftime("%Y.%m.%d-%H:%M:%S") + ".csv"
    
    def __call__(self):
        global fileName
        time_passed = datetime.now() - self._started_at
        if time_passed.total_seconds() > 120:
            self._started_at = datetime.now()
            fileName = datetime.now().strftime("%Y.%m.%d-%H.%M.%S") + ".csv"
            return fileName
        return fileName

value = TimedValue()

def write(data):
    # print "Data", data
    timeStamp = datetime.now().strftime("%Y.%m.%d-%H:%M:%S.%f")
    with open(value(), 'a') as file:
        file.write(timeStamp + ", " + str(data)+ "\n")
