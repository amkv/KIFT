from text2int import *
from badinput import *
import webbrowser
import os
import sys
from parser import *
from pprint import pprint
from google import *
import random

DEBUG = True

def print_debug_parser(text):
    global DEBUG
    if DEBUG:
        print text

def actionParser(text):
    text = text.lower()
    text = text.strip()
    string = list(text2int(text).split(' '))
    print("text=" + text)
    for each in string:
        if text.find("hello") != -1:
            hello = [
            'Hello! But leave me alone',
            'Hello, there',
            'Nice to hear you',
            'Hi'
            ]
            secure_random = random.SystemRandom()
            return secure_random.choice(hello)

        elif text.find("play") != -1 or (text.find("music") != -1 or text.find("jazz") != -1):
            webbrowser.open('file://' + os.getcwd() + "/src/server_src/data/strange_fruit.mp3")
            return "Music was played";

        elif text.find("set") != -1 and (text.find("alarm") != -1 or text.find("timer") != -1):
            second = timeParser(text)
            if second > 0:
                runTimer(second)
            return "Timer was set";



        # elif text.find("search") != -1 and text.find("web") != -1:
        #     webbrowser.open('https://www.google.com/webhp#q=%s' % text[8:])
        #     return "Google search done"

        elif text.find("google") != -1:
            google_pos = text.find("google") + 7
            text = text.replace(" ", "+")
            text = text.strip()
            webbrowser.open('https://www.google.com/#q=' + text[google_pos:])
            return "Search was done"

        elif text.find("joke") != -1:
            jokes = ['Past, present and future walk into a bar. It was tense.',
                     'Five out of six people agree that Russian Roulette is safe.',
                     'What did one snowman say to the other? -Do you smell carrots?'
                    ]
            return (random.choice(jokes))

        elif text.find("what") != -1:
            if text.find("forty") != -1 and text.find("two") != -1:
                return "Forty two is an innovative coding college producing the next generation of software engineers and programmers"

            elif text.find("time") != -1 and text.find("is") != -1:
                ret = "Today is" + d.strftime("%A %d. %B %Y")
                return ret

        elif text.find("open") != -1 and text.find("browser") != -1:
            webbrowser.open('http://ya.ru')
            return "Browser was open"

        elif text.find("brightness") != -1 or text.find("luminosity") != -1:
            if text.find("reduce") != -1:
                os.system("brightness 0.3")
                return ("Brightness decreased")
            elif text.find("increase") != -1:
                os.system("brightness 0.8")
                return ("Brightness increased")

        return badinput()


# def actionParser(text):
#     print_debug_parser('>>>>>>>>>>>>>>>>>>: ' + text)
#     if '(null)' in text:
#         print_debug_parser('>>>>>>>>>>>>>>>>>>: NULL input')
#         return badinput()
#     string = iter(text2int(text).split(' '))
#     for each in string:
#         if 'hello' in each:
#             print_debug_parser('>>>>>>>>>>>>>>>>>>: HELLO parser')
#             return "hello you"
#         elif "set" in each:
#             print_debug_parser('>>>>>>>>>>>>>>>>>>: SET parser')
#             each = next(string)
#             if "timer" in each:
#                 print_debug_parser('>>>>>>>>>>>>>>>>>>: SET TIMER parser')
#                 second = timeParser(text)
#                 if second > 0:
#                     runTimer(second)
#                 return "Timer was set";
#             if "alarm" in each or "an" in each:
#                 print_debug_parser('>>>>>>>>>>>>>>>>>>: ALARM parser')
#                 if "an" in each:
#                     each = next(string)
#                     if not "alarm" in each:
#                         return "Bad input"
#                     second = timeParser(text)
#                     if second > 0:
#                         runAlarm(second)
#                         return "Alarm was set";
#         elif "play" in each or "playing" in each:
#             print_debug_parser('>>>>>>>>>>>>>>>>>>: PLAY parser')
#             each = next(string)
#             if "music" in each or "jazz" in each:
#                 print_debug_parser('>>>>>>>>>>>>>>>>>>: PLAY MUSIC parser')
#                 os.system("play strange_fruit.mp3")
#                 return "Music was played";
#         elif "search" in each:
#             print_debug_parser('>>>>>>>>>>>>>>>>>>: SEARCH parser')
#             each = next(string)
#             if "web" in each or "the" in each:
#                 if "the" in each:
#                     each = next(string)
#                     if not "web" in each:
#                         return "Bad input"
#                 each = next(next(string))
#                 webbrowser.open('https://www.google.com/webhp#q=%s' % each)
#                 return "Google search done"
#             else:
#                 return "No search today"
#         elif "google" in each:
#             print_debug_parser('>>>>>>>>>>>>>>>>>>: GOOGLE parser')
#             each = next(string)
#             webbrowser.open('https://www.google.com/webhp#q=%s' % each)
#             return "Search was done"
#         elif "tell" in each:
#             print_debug_parser('>>>>>>>>>>>>>>>>>>: TELL parser')
#             each = next(string)
#             if "me" in each or "joke" in each:
#                 if "me" in each:
#                     each = next(string)
#                     if not "joke":
#                         return "Bad input"
#                     return ("Past, present and future walk into a bar. It was tense.")
#         elif "what" in each:
#             print_debug_parser('>>>>>>>>>>>>>>>>>>: WHAT parser')
#             each = next(string)
#             if "is" in each:
#                 each = next(string)
#                 if "forty" in each or "42" in each:
#                     each = next(string)
#                     if "two" in each:
#                         if not "two" in each:
#                             return "Bad input"
#                     return "Forty two is an innovative coding college producing the next generation of software engineers and programmers"
#             if "time" in each:
#                 each = next(string)
#                 if "is" in each:
#                     each = next(string)
#                     if not "it" in each:
#                         return "Bad input"
#                     ret = "Today is" + d.strftime("%A %d. %B %Y")
#                     return ret
#         else:
#             return badinput()
