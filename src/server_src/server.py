#! /usr/bin/python
# -*- coding: utf-8 -*-

import shutil
import sys
import os

from myserver import *

def set_folder(path, folder):
    """check folder, delete if exist"""
    if os.path.exists(path + folder):
        shutil.rmtree(path + folder)
    os.mkdir(path + folder)

def main(argv):
    if len(argv) != 2:
        print_usage()
    path = os.getcwd() + '/src/server_src/static/'
    host = '127.0.0.1'
    incoming_folder = 'incoming'
    outgoing_folder = 'outgoing'
    history_folder = 'history'
    set_folder(path, incoming_folder)
    set_folder(path, outgoing_folder)
    set_folder(path, history_folder)
    port = set_port(argv[1])
    check_port_is_open(host, port)
    run_the_server(port, path, incoming_folder, outgoing_folder)

if __name__ == '__main__':
    main(sys.argv)
