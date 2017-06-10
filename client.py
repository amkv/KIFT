#! /usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
import json

file = os.getcwd() + '/' + 'train/1_hello.wav'
upload_url = 'http://127.0.0.1:4040/'

file_ = {'file': (file, open(file, 'rb'))}
r = requests.post(upload_url, files=file_).text

# j = json.load(r)

print (r)
