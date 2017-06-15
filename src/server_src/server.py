#! /usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, send_from_directory, make_response, send_file
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
import random


# from sqlalchemy import create_engine
# from flask.ext.jsonpify import jsonify

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
    if os.path.exists(PATH + LOG_FOLDER):
        shutil.rmtree(PATH + LOG_FOLDER)
    os.mkdir(PATH + UPLOAD_FOLDER)
    os.mkdir(PATH + OUTGOING_FOLDER)
    os.mkdir(PATH + LOG_FOLDER)

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

    output_from_bla = subprocess.check_output('./bla toto.wav', shell=True)

    print("\n\n")
    print(output_from_bla)
    # otgoing_audio = filename + '.mp3'
    # text_to_client = parser(output_from_bla)
    data['filePath_input'] = "toto.wav"
    data['text_input'] = output_from_bla

    # ft_handler(text_input);

    tts = gTTS(text="return output", lang='en')
    tts.save("src/server_src/static/outgoing/toto_output.mp3")


    # json = ft_action(data['filePath_input'])
    data['filePath_output'] = "toto_output.mp3"
    data['text_output'] = "return output"

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

def text2int (textnum, numwords={}):
    if not numwords:
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)

    ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    # textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ""
    onnumber = False
    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in numwords:
                if onnumber:
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
            else:
                scale, increment = numwords[word]

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True

    if onnumber:
        curstring += repr(result + current)

    return curstring

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

def actionParser(text):
    text = text.lower()
    string = iter(text2int(text).split(' '))

    for each in string:
        if 'hello' in each:
            return "hello you"
        elif "set" in each:
            each = next(string)
            if "timer" in each:
                second = timeParser(text)
                if second > 0:
                    runTimer(second)
                return "Timer was set";
            if "alarm" in each or "an" in each:
                if "an" in each:
                    each = next(string)
                    if not "alarm" in each:
                        return "Bad input"
                    second = timeParser(text)
                    if second > 0:
                        runAlarm(second)
                        return "Alarm was set";
        elif "play" in each or "playing" in each:
            each = next(string)
            if "music" in each or "jazz" in each:
                os.system("play strange_fruit.mp3")
                return "Music was played";
        elif "search" in each:
            each = next(string)
            if "web" in each or "the" in each:
                if "the" in each:
                    each = next(string)
                    if not "web" in each:
                        return "Bad input"
                each = next(next(string))
                webbrowser.open('https://www.google.com/webhp#q=%s' % each)
                return "Google search done"
        elif "google" in each:
            each = next(string)
            webbrowser.open('https://www.google.com/webhp#q=%s' % each)
            return "Search was done"
        elif "tell" in each:
            each = next(string)
            if "me" in each or "joke" in each:
                if "me" in each:
                    each = next(string)
                    if not "joke":
                        return "Bad input"
                    return ("Past, present and future walk into a bar. It was tense.")
        elif "what" in each:
            each = next(string)
            if "is" in each:
                each = next(string)
                if "forty" in each or "42" in each:
                    each = next(string)
                    if "two" in each:
                        if not "two" in each:
                            return "Bad input"
                    return "Forty two is an innovative coding college producing the next generation of software engineers and programmers"
            if "time" in each:
                each = next(string)
                if "is" in each:
                    each = next(string)
                    if not "it" in each:
                        return "Bad input"
                    ret = "Today is" + d.strftime("%A %d. %B %Y")
                    return ret

        else:
            badinput = [
            'Oh, No, I don\'t get it',
            'Bad input',
            'NO!',
            'Sorry',
            'Marry me first',
            'I am too lasy today',
            'Booooring']
            return random.choice(badinput)

# #######################################################################

# def parser(text):
#     if 'hello' in text:
#         result = "oh! hello, nice to see you!"
#     else:
#         result = "Sorry, you are bad programmers, very bad programmers"
#     save_to_log(text, result)
#     return result

def handler(filename):
    output_from_bla = subprocess.check_output('./bla %(UPLOAD_FOLDER)s/%(filename)s' % {'UPLOAD_FOLDER': UPLOAD_FOLDER, 'filename': filename}, shell=True)
    otgoing_audio = filename + '.mp3'
    save_to_log(output_from_bla)
    text_to_client = actionParser(output_from_bla)
    tts = gTTS(text=text_to_client, lang='en')
    tts.save(OUTGOING_FOLDER + '/' + otgoing_audio)
    response = make_response(open(OUTGOING_FOLDER + '/' + otgoing_audio).read())
    response.headers['Content-Type'] = 'audio/mp3'
    response.headers['Content-Disposition'] = 'attachment; filename=' + otgoing_audio
    return response

if __name__ == '__main__':
    """main method."""
    if len(sys.argv) != 2:
        print_usage()
    set_folders()
    port = set_port(sys.argv[1])
    check_port_is_open(port)
    app.run(port = port)
