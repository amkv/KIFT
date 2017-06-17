from text2int import *
from badinput import *
import webbrowser
import os
import sys
from parser import *
from pprint import pprint
from google import *
import random
from time import gmtime, strftime
from alarm import *
from text2int import *

def actionParser(text):
    text = text2int(text).strip()
    string = list(text.split(' '))

# ok ################################################################

    if 'hello' in string[0]:
        hello = [
        'Hello! But leave me alone',
        'Hello, there',
        'Nice to hear you',
        'Hi'
        ]
        secure_random = random.SystemRandom()
        return secure_random.choice(hello)


    elif 'play' in string[0] or 'music' in string[0] or 'jazz' in string[0]:
        webbrowser.open('file://' + os.getcwd() + "/src/server_src/data/strange_fruit.mp3")
        return "OK";

    elif 'joke' in string[0]:
        jokes = ['Past, present and future walk into a bar. It was tense.',
                 'Five out of six people agree that Russian Roulette is safe.',
                 'What did one snowman say to the other? -Do you smell carrots?'
                ]
        secure_random = random.SystemRandom()
        return secure_random.choice(jokes)

    elif 'what' in string[0]:
        if "forty" in string and "two" in string:
            return "Forty two is an innovative coding college producing the next generation of software engineers and programmers"

        elif "time" in string:
            ret = "Time is" + strftime(" %H:%M %p")
            return ret
        else:
            return badinput()

    elif 'google' in string[0]:
        if len(string) <= 1:
            webbrowser.open('https://www.google.com/')
            return "Google yourself"
        query = ' '.join(string[1:])
        query = query.replace(" ", "+")
        query = query.strip()
        webbrowser.open('https://www.google.com/#q=' + query)
        return "Search was done"

    elif "brightness" in string[0]:
         os.system("brightness 1")
         return ("I like California style")

    elif 'no' in string[0] and 'voice' in string[1]:
        return "You did not say anything. Sometimes it's better to be silent"

# ###################################################################

    elif 'set' in string[0]:
        if len(string) <= 1:
            return "Nothing to set";
        if 'alarm' in string[1] or 'timer' in string[1]:
            second = timeParser(text)
            if second > 0:
                runTimer(second)
            else:
                return "Bad timer"
            return "Timer was set";
        else:
            return "Nothing to set"

    # elif text.find("open") != -1 and text.find("browser") != -1:
    #     webbrowser.open('http://ya.ru')
    #     return "Browser was open"

    # elif text.find("search") != -1 and text.find("web") != -1:
    #     webbrowser.open('https://www.google.com/webhp#q=%s' % text[8:])
    #     return "Google search done"

    return badinput()
