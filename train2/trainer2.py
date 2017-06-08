#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
import os

path = ''

def read_file():
    global path
    with open(path + "old.transcription", "r") as ins:
        for line in ins:
            quoted = line.partition('(')[-1].rpartition(')')[0]
            text = line.partition('<s>')[-1].rpartition('</s>')[0]
            print("-----------")
            print(quoted)
            print(text)
            raw_input('ready for next? ctr-c for stop recording')
            print("-----------")
            os.system('rec -r 16k -e signed-integer -b 16 -c 1 %(path)s%(quoted)s.wav' % {'path' : path, 'quoted' : quoted})

def main():
    read_file()

if __name__ == "__main__":
    main()
