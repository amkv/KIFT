#! /usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
import shutil
import sys
import os
import json
from flask import render_template
import socket
# from sqlalchemy import create_engine
# from flask.ext.jsonpify import jsonify

# Constant variables
app = Flask(__name__)
api = Api(app)
PATH = os.getcwd() + '/'
# Folder for upload incoming wav files
UPLOAD_FOLDER = 'uploaded'
OUTGOING_FOLDER = 'outgoing'
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

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handler(filename):
    response = json.dumps({'status': 'ok', 'wav': filename, 'link': 'http://google.com'}, sort_keys=True, indent=4)
    return response

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return handler(filename)
#     return '''
#     <!doctype html>
#     <title>KIFT server side</title>
#     <h1>Upload wav file</h1>
#     <form method=post enctype=multipart/form-data>
#       <p><input type=file name=file>
#          <input type=submit value=Upload>
#     </form>
#     '''

@app.route('/')
def upload(my_callback=None):
    return render_template("upload.html", my_callback="hello")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
      # Open file and write binary (blob) data
      f = open('./commands_log/command_.wav', 'wb') #generate_name
      f.write(request.data)
      f.close()
    #   text = os.system(bla command_.wav)
    #   response = ft_handle(text)
    #         set_the_timer()
    #         return "OK"
    #   response

    #   Tweak to get the file .wav with the good header. Need to find a fix
    #   os.system('ffmpeg -y -i ./commands_log/command_.wav -f s16le -acodec pcm_s16le ./commands_log/output.pcm')
    #   os.system('ffmpeg -y -f s16le -ar 44.1k -ac 1 -i ./commands_log/output.pcm ./commands_log/command_.wav')
    #   text = os.system('./bla ./commands_log/command_.wav')
    #   print(text)
    #   return(text)
      return "Binary message written!"

def check_port_is_open(port):
    """Check is socket port opened"""
    global HOST
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((HOST, port))
    if result == 0:
       print "Port %(port)s is already opened." % {'port': port}
       sys.exit(1)

if __name__ == '__main__':
    """main method."""
    if len(sys.argv) != 2:
        print_usage()
    set_folders()
    port = set_port(sys.argv[1])
    check_port_is_open(port)
    app.run(port = port)
