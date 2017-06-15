#!/usr/bin/python env

import os
import time
import webbrowser
from datetime import datetime
from numParser import text2int

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
    #.strftime('%Y-%m-%d %H:%M:%S')

def actionParser(text):
    text = text.lower()
    string = iter(text2int(text).split(' '))
    for each in string:
        if "set" in each:
            each = next(string)
            if "timer" in each:
                second = timeParser(text)
                if second > 0:
                    runTimer(second)
                return "Timer was set";
            if "alarm" in each or "an" in each:
                if "an" in each:
                    each = next(string)
                    if not "alarm" in each:
                        return "Bad input"
                    second = timeParser(text)
                    if second > 0:
                        runAlarm(second)
                        return "Alarm was set";
        elif "play" in each:
            each = next(string)
            if "music" in each or "jazz" in each:
                os.system("play strange_fruit.mp3")
                return "Music was played";
        elif "search" in each:
            each = next(string)
            if "web" in each or "the" in each:
                if "the" in each:
                    each = next(string)
                    if not "web" in each:
                        return "Bad input"
                each = next(next(string))
                webbrowser.open('https://www.google.com/webhp#q=%s' % each)
                return "Google search done"
        elif "google" in each:
            each = next(string)
            webbrowser.open('https://www.google.com/webhp#q=%s' % each)
            return "Search was done"
        elif "tell" in each:
            each = next(string)
            if "me" in each or "joke" in each:
                if "me" in each:
                    each = next(string)
                    if not "joke":
                        return "Bad input"
                    return ("Past, present and future walk into a bar. It was tense.")
        elif "what" in each:
            each = next(string)
            if "is" in each:
                each = next(string)
                if "forty" in each or "42" in each:
                    each = next(string)
                    if "two" in each:
                        if not "two" in each:
                            return "Bad input"
                    return "Forty two is an innovative coding college producing the next generation of software engineers and programmers"
            if "time" in each:
                each = next(string)
                if "is" in each:
                    each = next(string)
                    if not "it" in each:
                        return "Bad input"
                    ret = "Today is" + d.strftime("%A %d. %B %Y")
                    return ret

        else:
            return ("Bad input")

# print actionParser("what is 42")
# print actionParser("set timer")
# print runAlarm(3000)
print actionParser("what time is it")
