import datetime
import time
fileName = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S") + ".fc32"
class TimedValue:

    def __init__(self):
        global fileName 
        self._started_at = datetime.datetime.now()
        fileName = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S") + ".fc32"

    def __call__(self):
        global fileName 
        time_passed = datetime.datetime.now() - self._started_at
        if time_passed.total_seconds() > 30:
            self._started_at = datetime.datetime.now()
            fileName = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S") + ".fc32"
            return fileName
        return fileName

value = TimedValue()

# t_end = time.time() + 60 * 15
# def getValue():
#     while true:
#         return value()


# import sched, time
# fileName = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S") + ".fc32"
# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc): 
#     global fileName 
#     print "Doing stuff..."
#     # do your stuff
#     fileName = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S") + ".fc32"
#     s.enter(300, 1, do_something, (sc,))

# s.enter(300, 1, do_something, (s,))
# s.run()

# import threading
# # fileName = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S") + ".fc32"
# def hello_world():
#     global fileName 
#     threading.Timer(30.0, hello_world).start() # called every minute
#     value()
#     # fileName = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S") + ".fc32"
#     print "Doing stuff..." + fileName

# hello_world()