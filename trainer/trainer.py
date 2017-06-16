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
    try:
        new_file = open(path + name, 'a')
        print('file %(path)s%(name)s opened' % {'path' : path, 'name' : name})
    except:
        print('can\'t create %(path)s%(name)s' % {'name' : name, 'path' : path})
        sys.exit(0)
    new_file.close()

def append_to_transcription(path, transcription, text, wavname):
    file = open(path + transcription, 'a')
    file.write('<s> %(text)s </s> (%(wavname)s)\n' % {'text' : text, 'wavname' : wavname})
    file.close()

def append_to_fileids(path, fileids, wavname):
    file = open(path + fileids, 'a')
    file.write('%(wavname)s\n' % {'wavname' : wavname})
    file.close()

def set_wavname(text, counter):
    wavname = text.replace(' ', '_')
    if len(wavname) > 10:
        wavname = wavname[:9]
    wavname = str(counter) + '_' + wavname
    return wavname

def new_voice(path, wavname):
    try:
        os.system('rec -r 16000 -e signed-integer -b 16 -c 1 %(path)s%(wavname)s.wav' % {'path' : path, 'wavname' : wavname})
    except:
        print('can\'t create %(path)s%(name)s' % {'wavname' : wavname, 'path' : path})
        sys.exit(0)

def set_counter(path, fileids):
    counter = 0
    file = open(path + fileids, 'rb')
    lines = file.readlines()
    if lines:
        last = lines[-1].split('_')
        counter = int(last[0])
    return counter

def close_file(transcription_file, fileids_file):
    close(transcription_file)
    close(fileids_file)

def get_last_text(path, transcription):
    file = open(path + transcription, 'rb')
    lines = file.readlines()
    if lines:
        last = lines[-1].partition('<s> ')[-1].rpartition(' </s>')[0]
    else:
        print('write some text before repeat it')
        return None
    return last

def main():
    os.system('clear')
    folder = 'train'
    path = folder + '/'
    transcription = 'text.transcription'
    fileids = 'text.fileids'
    print('trainer v0.1')
    print('-----------------------------------------')
    create_folder(folder)
    create_file(path, transcription)
    create_file(path, fileids)
    counter = set_counter(path, fileids)
    repeats = 1
    while True:
        text = raw_input('>')
        counter += 1
        if len(text) < 1:
            text = get_last_text(path, transcription)
            if not text:
                continue
            repeats += 1
        else:
            repeats = 1
        if '!' in text:
            sys.exit(0)
            print('ok, exit')
        os.system('clear')
        print('----------------------------------------\n\n')
        print (text + '\n\n')
        print('----------------------------------------\n')
        print('|   ' + str(repeats))
        print('----------------------------------------\n')
        wavname = set_wavname(text, counter)
        append_to_transcription(path, transcription, text, wavname)
        append_to_fileids(path, fileids, wavname)
        new_voice(path, wavname)

if __name__ == "__main__":
    main()
