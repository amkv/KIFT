#! /usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
from random import randrange
import sys

def new_voice(path, wavname):
    try:
        os.system('rec -r 16000 -e signed-integer -b 16 -c 1 %(path)s%(wavname)s.wav' % {'path' : path, 'wavname' : wavname})
    except:
        print('can\'t create %(path)s%(name)s' % {'wavname' : wavname, 'path' : path})
        sys.exit(0)

def print_usage():
    """show usage and exit"""
    print ('usage: client.py <port number>')
    sys.exit(0)

def set_port(argv):
    """convert argument, check number in range, return port"""
    port = int(argv)
    if port <= 100 or port >= 65535:
        print_usage()
    else:
        return port

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
    port = set_port(sys.argv[1])
    path = os.getcwd() + '/query/'
    wavname = str(randrange(1000, 3000))
    file = path + wavname + '.wav'
    while True:
        text = raw_input('> Ask me something after <enter>\n')
        if len(text) < 1:
            try:
                new_voice(path, wavname)
                # print "> [file recorded]"
            except:
                pass
                # print("> [can't record voice]")
            upload_url = 'http://127.0.0.1:' + str(port) + '/test'
            file_ = {'file': (file, open(file, 'rb'))}
            try:
                r = requests.post(upload_url, files=file_)
                # print "> [requested]"
            except:
                pass
                # print("> [can't send request to server]")
            try:
                with open ('test.mp3', 'wb') as f:
                    f.write(r.content)
                    # print "> [file created]"
            except:
                pass
                # print("> [can't create file]")
            try:
                os.system('play test.mp3')
                # print "> [file played]"
            except:
                pass
                # print "> [can't play file]"
        if '!' in text:
            break
