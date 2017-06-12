#! /usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
import json
import sys

def main(argv):
    if len(argv) != 2:
        print "usage: client <port>"
        sys.exit(0)
    file = os.getcwd() + '/' + 'train/1_hello.wav'
    port = int(sys.argv[1])
    upload_url = 'http://127.0.0.1' + str(port) + '/upload'
    file_ = {'file': (file, open(file, 'rb'))}
    try:
        r = requests.post(upload_url, files=file_).text
    except:
        print "bad connection"
        sys.exit(0)
    print (r)

if __name__ == "__main__":
    main(sys.argv)
