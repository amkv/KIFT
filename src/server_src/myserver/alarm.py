import webbrowser
from text2int import *

def timeParser(text):
    string = iter(text2int(text).split(' '))
    hour = 0
    minute = 0
    second = 0
    for each in string:
        try:
            temp = int(each)
        except:
            continue
        if temp > 0:
            each = next(string)
            if ('hour' or 'hours') in each:
                hour = temp
            elif ('minute' or 'minutes') in each:
                minute = temp
            elif ('second' or 'seconds') in each:
                second = temp
    return second + (minute * 60) + (hour * 3600)

def runTimer(second):
    webbrowser.open('http://e.ggtimer.com/%d' % second)

def runAlarm(second):
    curTime = datetime.now()
    print curTime
    type(curTime)
