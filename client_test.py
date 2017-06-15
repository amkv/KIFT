#! /usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
from random import randrange

def new_voice(path, wavname):
    try:
        os.system('rec -r 16k -e signed-integer -b 16 -c 1 %(path)s%(wavname)s.wav' % {'path' : path, 'wavname' : wavname})
    except:
        print('can\'t create %(path)s%(name)s' % {'wavname' : wavname, 'path' : path})
        sys.exit(0)

path = os.getcwd() + '/query/'
wavname = str(randrange(1000, 3000))
file = path + wavname + '.wav'
while True:
    text = raw_input('> Ask me something after <enter>\n')
    if len(text) < 1:
        new_voice(path, wavname)
        print "file recorded"
        upload_url = 'http://127.0.0.1:4040/test'
        file_ = {'file': (file, open(file, 'rb'))}
        r = requests.post(upload_url, files=file_)
        print "requested"
        with open ('test.mp3', 'wb') as f:
            f.write(r.content)
        print "file created"
        os.system('play test.mp3')
        print "file created"
    if '!' in text:
        break
