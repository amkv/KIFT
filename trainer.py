#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import sys

def create_folder(name):
    if not os.path.exists(name):
        try:
            os.makedirs(name)
            print('folder %(name)s created' % {'name' : name})
        except:
            print('can\'t create %(name)s' % {'name' : name})
            sys.exit(0)
    else:
        print('folder %(name)s already exist' % {'name' : name})

def create_file(path, name):
    print path + name
    try:
        new_file = open(path + name, 'w')
    except:
        print('can\'t create %(path)s%(name)s' % {'name' : name, 'path' : path})
        sys.exit(0)
    return new_file

def append_to_transcription(file, text, wavname):
    file.write('<s> %(text)s </s> (%(wavname)s)\n' % {'text' : text, 'wavname' : wavname})

def append_to_fileids(file, wavname):
    file.write('%(wavname)s\n' % {'wavname' : wavname})

def set_wavname(text, counter):
    wavname = text.replace(' ', '_')
    if len(wavname) > 10:
        wavname = wavname[:9]
    wavname = str(counter) + '_' + wavname
    return wavname

def new_voice(path, wavname):
    try:
        os.system('rec -r 16k -e signed-integer -b 16 -c 1 %(path)s%(wavname)s.wav' % {'path' : path, 'wavname' : wavname})
    except:
        print('can\'t create %(path)s%(name)s' % {'wavname' : wavname, 'path' : path})
        sys.exit(0)

def main():
    folder = 'train'
    path = folder + '/'
    transcription = 'text.transcription'
    fileids = 'text.fileids'
    print('trainer v0.1')
    print('-----------------------------------------')
    create_folder(folder)
    transcription_file = create_file(path, transcription)
    fileids_file = create_file(path, fileids)

    counter = 0
    while True:
        text = raw_input('>')
        if len(text) < 1:
            continue
        counter += 1
        wavname = set_wavname(text, counter)
        append_to_transcription(transcription_file, text, wavname)
        append_to_fileids(fileids_file, wavname)
        new_voice(path, wavname)

if __name__ == "__main__":
    main()

    # text = None
    # holder = None
    # while True:
    #     if text == None:
    #         text = raw_input('>')
    #     else:
    #         holder = text
    #         text = raw_input('>')
    #     if '!' in text:
    #         print('end of training')
    #         sys.exit(0)
    #     elif '#' in text:
    #         print('ok, new text')
    #         text = raw_input('input new text:')
    #         holder = None
    #     else:
    #         if holder != None:
    #             print(holder)
    #         else:
    #             print('empty holder')
    #         print('continue training with')
