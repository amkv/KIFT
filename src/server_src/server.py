#! /usr/bin/python
# -*- coding: utf-8 -*-

import shutil
import sys
import os

from myserver import *

# Constant variables


# Folder for upload incoming wav files


# SERVER_FOLDER = PATH + 'src/server_src/'

# def save_to_log(text):
#     global PATH
#     global LOG_FOLDER
#     global LOG_FILE
#     logfile = open(PATH + LOG_FOLDER + '/' + LOG_FILE, 'a')
#     logfile.write(text)
#     logfile.close()

def set_folder(path, folder):
    """check folder, delete if exist"""
    if os.path.exists(path + folder):
        shutil.rmtree(path + folder)
    os.mkdir(path + folder)

# #######################################################################

def main(argv):
    if len(argv) != 2:
        print_usage()
    path = os.getcwd() + '/'
    upload_folder = 'uploaded'
    outgoing_folder = 'outgoing'
    log_folder = 'history'
    LOG_FILE = 'logs'
    host = '127.0.0.1'
    set_folder(path, upload_folder)
    set_folder(path, outgoing_folder)
    set_folder(path, log_folder)
    port = set_port(argv[1])
    check_port_is_open(host, port)
    run_the_server(port, path, upload_folder, outgoing_folder)

if __name__ == '__main__':
    main(sys.argv)
