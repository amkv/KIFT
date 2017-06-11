#! /usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, render_template
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
import shutil
import sys
import os
# from sqlalchemy import create_engine
import json
# from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)
PATH = os.getcwd() + '/'
UPLOAD_FOLDER = 'uploaded'
ALLOWED_EXTENSIONS = set(['wav'])
app.config['UPLOAD_FOLDER'] = PATH + UPLOAD_FOLDER

def set_folders():
    global PATH
    global UPLOAD_FOLDER
    if os.path.exists(PATH + UPLOAD_FOLDER):
        shutil.rmtree(PATH + UPLOAD_FOLDER)
    os.mkdir(PATH + UPLOAD_FOLDER)

def print_usage():
    print ('usage: server.py <port number>')
    sys.exit(0)

def set_port(argv):
    port = int(argv)
    if port <= 100 or port >= 63000:
        print_usage()
    else:
        return port

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handler(filename):

    response = json.dumps({'status': 'ok', 'wav': filename, 'link': 'http://google.com'}, sort_keys=True, indent=4)
    return response

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
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

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
      # Open file and write binary (blob) data
      f = open('./file.wav', 'wb')
      f.write(request.data)
      f.close()
    #   Tweak to get the file .wav with the good header. Need to find a fix
      os.system('ffmpeg -y -i file.wav -f s16le -acodec pcm_s16le output.pcm')
      os.system('ffmpeg -y -f s16le -ar 44.1k -ac 1 -i output.pcm file_FIXED.wav')

      return "Binary message written!"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage()
    set_folders()
    port = set_port(sys.argv[1])
    app.run(port = port)
