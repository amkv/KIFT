from text2int import *
from badinput import *
import webbrowser
import os
import sys
# import timeParser

DEBUG = True

def print_debug_parser(text):
    global DEBUG
    if DEBUG:
        print text

def actionParser(text):
    print_debug_parser('>>>>>>>>>>>>>>>>>>PARSER')
    print_debug_parser('>>>>>>>>>>>>>>>>>>: ' + text)
    if '(null)' in text:
        print_debug_parser('>>>>>>>>>>>>>>>>>>: NULL input')
        return badinput()
    string = iter(text2int(text).split(' '))
    for each in string:
        if 'hello' in each:
            print_debug_parser('>>>>>>>>>>>>>>>>>>: HELLO parser')
            return "hello you"
        elif "set" in each:
            print_debug_parser('>>>>>>>>>>>>>>>>>>: SET parser')
            each = next(string)
            if "timer" in each:
                print_debug_parser('>>>>>>>>>>>>>>>>>>: SET TIMER parser')
                second = timeParser(text)
                if second > 0:
                    runTimer(second)
                return "Timer was set";
            if "alarm" in each or "an" in each:
                print_debug_parser('>>>>>>>>>>>>>>>>>>: ALARM parser')
                if "an" in each:
                    each = next(string)
                    if not "alarm" in each:
                        return "Bad input"
                    second = timeParser(text)
                    if second > 0:
                        runAlarm(second)
                        return "Alarm was set";
        elif "play" in each or "playing" in each:
            print_debug_parser('>>>>>>>>>>>>>>>>>>: PLAY parser')
            each = next(string)
            if "music" in each or "jazz" in each:
                print_debug_parser('>>>>>>>>>>>>>>>>>>: PLAY MUSIC parser')
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
            return badinput()
