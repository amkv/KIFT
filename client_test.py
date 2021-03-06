#! /usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
from random import randrange
import sys
import shutil
import socket

DEBUG = False

def new_voice(path, wavname):
    try:
        os.system('rec -r 16k -e signed-integer -b 16 -c 1 %(path)s%(wavname)s.wav' % {'path' : path, 'wavname' : wavname})
    except:
        print('can\'t create %(path)s%(name)s' % {'wavname' : wavname, 'path' : path})
        sys.exit(0)

def print_usage():
    """show usage and exit"""
    print ('usage: client.py <port number 1000 - 65535>')
    sys.exit(0)

def set_port(argv):
    """convert argument, check number in range, return port"""
    port = int(argv)
    if port <= 1000 or port >= 65535:
        print_usage()
    else:
        return port

def set_folder(path, folder):
    """check folder, delete if exist"""
    if os.path.exists(path + folder):
        shutil.rmtree(path + folder)
    os.mkdir(path + folder)
    return path + folder

def check_port_is_open(host, port):
    """Check is socket port opened"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        print "Port %(port)s is opened." % {'port': port}
    else:
        print "Port %(port)s is not opened." % {'port': port}
        sys.exit(1)

def print_debug(text):
    global DEBUG
    if DEBUG:
        print (text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
    host = '127.0.0.1'
    port = set_port(sys.argv[1])
    check_port_is_open(host, port)
    path = set_folder(os.getcwd(), '/query/')
    wavname = str(randrange(1000, 3000))
    file = path + wavname + '.wav'
    while True:
        text = raw_input('> Ask me something after <enter>\n')
        if len(text) < 1:
            try:
                new_voice(path, wavname)
                print_debug("> [file recorded]")
            except:
                pass
                print_debug("> [can't record voice]")
            upload_url = 'http://127.0.0.1:' + str(port) + '/manual'
            file_ = {'file': (file, open(file, 'rb'))}
            try:
                r = requests.post(upload_url, files=file_)
                print_debug("> [requested]")
            except:
                pass
                print_debug("> [can't send request to server]")
            try:
                with open (path + 'output_to_client.mp3', 'wb') as f:
                    f.write(r.content)
                    print_debug("> [file created]")
            except:
                pass
                print_debug("> [can't create file]")
            try:
                os.system('play ' + path + 'output_to_client.mp3')
                print_debug("> [file played]")
            except:
                pass
                print_debug("> [can't play file]")
        if '!' in text:
            break
