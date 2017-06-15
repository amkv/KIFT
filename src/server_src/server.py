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
import random
import webbrowser


from myserver import *

# Constant variables
app = Flask(__name__)
api = Api(app)
PATH = os.getcwd() + '/'
print PATH
# Folder for upload incoming wav files
UPLOAD_FOLDER = 'uploaded'
OUTGOING_FOLDER = 'outgoing'
SERVER_FOLDER = PATH + 'src/server_src/'
LOG_FOLDER = 'history'
LOG_FILE = 'logs'
HOST = '127.0.0.1'
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
    if os.path.exists(PATH + LOG_FOLDER):
        shutil.rmtree(PATH + LOG_FOLDER)
    os.mkdir(PATH + UPLOAD_FOLDER)
    os.mkdir(PATH + OUTGOING_FOLDER)
    os.mkdir(PATH + LOG_FOLDER)

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

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # f = open(PATH + UPLOAD_FOLDER + '/' + "to_be_analized.wav", 'wb')
    # f.write(request.data)
    # f.close()
    f = open('toto.wav', 'wb')
    f.write(request.data)
    f.close()
    data = {};
    # data['text'] = "salut asdfsdaf asdf  asdf"


    os.system('sox toto.wav -r 16000 toto_converted.wav')
    # os.system('ffmpeg -y -i toto.wav -f s16le -acodec pcm_s16le toto.pcm')
    # os.system('ffmpeg -y -f s16le -ar 44.1k -ac 1 -i toto.pcm toto.wav')

    output_from_bla = subprocess.check_output('./bla toto_converted.wav', shell=True)
    text_output = actionParser(output_from_bla)

    print("\n\n")
    print(output_from_bla)
    # otgoing_audio = filename + '.mp3'
    # text_to_client = parser(output_from_bla)
    data['filePath_input'] = "toto.wav"
    data['text_input'] = output_from_bla

    # ft_handler(text_input);

    file_name_output = str(randrange(1000, 3000)) + str(int(time.time())) + '.mp3'

    tts = gTTS(text=text_output, lang='en')
    tts.save("src/server_src/static/outgoing/" + file_name_output)


    # json = ft_action(data['filePath_input'])
    data['filePath_output'] = file_name_output
    data['text_output'] = text_output

    json_data = json.dumps(data)

    # return json_data
    return json_data

@app.route('/test', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = str(randrange(1000, 3000)) + str(int(time.time()))
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

# def save_to_log(text, result):
#     global PATH
#     global LOG_FOLDER
#     global LOG_FILE
#     logfile = open(PATH + LOG_FOLDER + '/' + LOG_FILE, 'w')
#     logfile.write(text + '|' + result)
#     logfile.close()

def save_to_log(text):
    global PATH
    global LOG_FOLDER
    global LOG_FILE
    logfile = open(PATH + LOG_FOLDER + '/' + LOG_FILE, 'a')
    logfile.write(text)
    logfile.close()

# #######################################################################

def timeParser(text):
    string = iter(text2int(text).split(' '))
    hour = 0
    minute = 0
    second = 0
    for each in string:
        try:
            temp = int(each)
        except:
            continue
        if temp > 0:
            each = next(string)
            if ('hour' or 'hours') in each:
                hour = temp
            elif ('minute' or 'minutes') in each:
                minute = temp
            elif ('second' or 'seconds') in each:
                second = temp
    return second + (minute * 60) + (hour * 3600)

def runTimer(second):
    webbrowser.open('http://e.ggtimer.com/%d' % second)

def runAlarm(second):
    curTime = datetime.now()
    print curTime
    type(curTime)
    #.strftime('%Y-%m-%d %H:%M:%S')

# #######################################################################

if __name__ == '__main__':
    """main method."""
    if len(sys.argv) != 2:
        print_usage()
    set_folders()
    port = set_port(sys.argv[1])
    check_port_is_open(port)
    app.run(port = port)
