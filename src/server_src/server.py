#! /usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, send_from_directory
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
import shutil
import sys
import os
import json
from flask import render_template
import socket
from random import randrange, uniform
import time
import subprocess
from gtts import gTTS
# from sqlalchemy import create_engine
# from flask.ext.jsonpify import jsonify

# Constant variables
app = Flask(__name__)
api = Api(app)
PATH = os.getcwd() + '/'
# Folder for upload incoming wav files
UPLOAD_FOLDER = 'uploaded'
OUTGOING_FOLDER = 'outgoing'
SERVER_FOLDER = PATH + 'src/server_src/'
HOST = '127.0.0.1'
# Checker for upload method, only wav
# for example
# ALLOWED_EXTENSIONS = set(['wav', 'mp3'])
ALLOWED_EXTENSIONS = set(['wav'])
app.config['UPLOAD_FOLDER'] = PATH + UPLOAD_FOLDER

def set_folders():
    """check the folders, delete if exist"""
    global PATH
    global UPLOAD_FOLDER
    global OUTGOING_FOLDER
    if os.path.exists(PATH + UPLOAD_FOLDER):
        shutil.rmtree(PATH + UPLOAD_FOLDER)
    if os.path.exists(PATH + OUTGOING_FOLDER):
        shutil.rmtree(PATH + OUTGOING_FOLDER)
    os.mkdir(PATH + UPLOAD_FOLDER)
    os.mkdir(PATH + OUTGOING_FOLDER)

def print_usage():
    """show usage and exit"""
    print ('usage: server.py <port number>')
    sys.exit(0)

def set_port(argv):
    """convert argument, check number in range, return port"""
    port = int(argv)
    if port <= 100 or port >= 65535:
        print_usage()
    else:
        return port

def check_port_is_open(port):
    """Check is socket port opened"""
    global HOST
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((HOST, port))
    if result == 0:
        print "Port %(port)s is already opened." % {'port': port}
        sys.exit(1)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload(my_callback=None):
    return render_template("upload.html", my_callback="hello")

# ⚠️ Not Working ⚠️
# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#       # Open file and write binary (blob) data
#       global UPLOAD_FOLDER
#       print ('submit')
#       new_file = str(os.urandom())
#       f = open(PATH + UPLOAD_FOLDER + '/' + new_file, 'wb') #generate_name
#       f.write(request.data)
#       f.close()
#     #   text = os.system(bla command_.wav)
#     #   response = ft_handle(text)
#     #         set_the_timer()
#     #         return "OK"
#     #   response
#     #   print(text)
#     #   return(text)
#       return "Binary message written!"
# ⚠️ Not Working ⚠️


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    f = open(PATH + UPLOAD_FOLDER + '/' + "to_be_analized.wav", 'wb')
    f.write(request.data)
    f.close()
    # Analyse file with bla and return the answer
    return "Analyzed string goes theres"

@app.route('/test', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = str(randrange(1000, 3000)) + str(int(time.time())) + '.wav'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return handler(filename)
    return '''
    <!doctype html>
    <title>KIFT server side</title>
    <h1>Upload wav file</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

def handler(filename):
    output = subprocess.check_output('./bla %(UPLOAD_FOLDER)s/%(filename)s' % {'UPLOAD_FOLDER': UPLOAD_FOLDER, 'filename': filename}, shell=True)
    tts = gTTS(text=output, lang='en')
    tts.save(OUTGOING_FOLDER + '/' + filename + '.mp3')
    # return send_from_directory(PATH + 'uploaded/', filename)
    return send_from_directory(PATH + OUTGOING_FOLDER + '/', filename + '.mp3')

if __name__ == '__main__':
    """main method."""
    if len(sys.argv) != 2:
        print_usage()
    set_folders()
    port = set_port(sys.argv[1])
    check_port_is_open(port)
    app.run(port = port)


# link  = '127.0.0.1:4040/uploaded/' + filename
# response = json.dumps( \
# { \
# 'status': 'ok', \
# 'wav': filename, \
# 'link': link \
# }, \
# sort_keys=True, indent=4)
