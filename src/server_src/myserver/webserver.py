from flask import Flask, request, redirect, send_from_directory
from flask_restful import Api
from werkzeug.utils import secure_filename
import json
from flask import render_template
from random import randrange, uniform
import time
import random
import os
import subprocess
from myserver import *

app = Flask(__name__, template_folder='../templates', static_folder='../static')
api = Api(app)
ALLOWED_EXTENSIONS = set(['wav'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload(my_callback=None):
    return render_template("upload.html", my_callback="hello")
    # return 'ok'

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     # f = open(PATH + UPLOAD_FOLDER + '/' + "to_be_analized.wav", 'wb')
#     # f.write(request.data)
#     # f.close()
#     with open ('toto.wav', 'wb') as f:
#         f.write(request.data)
#         f.close()
#     # f = open('toto_1.wav', 'wb')
#     # f.write(request.data)
#     # f.close()
#     data = {};
#     # data['text'] = "salut asdfsdaf asdf  asdf"
#
#     # os.system('sox toto.wav -r 16000 toto_conv_sox.wav')
#     # os.system('ffmpeg -y -i toto.wav -f s16le -acodec pcm_s16le toto.pcm')
#     # os.system('ffmpeg -y -f s16le -ar 44.1k -ac 1 -i toto.pcm toto.wav')
#
#     output_from_bla = subprocess.check_output('./bla toto.wav', shell=True)
#     text_output = actionParser(output_from_bla)
#
#     print("\n\n")
#     print(output_from_bla)
#     # otgoing_audio = filename + '.mp3'
#     # text_to_client = parser(output_from_bla)
#     data['filePath_input'] = "toto.wav"
#     data['text_input'] = output_from_bla
#
#     # ft_handler(text_input);
#
#     file_name_output = str(randrange(1000, 3000)) + str(int(time.time())) + '.mp3'
#
#     tts = gTTS(text=text_output, lang='en')
#     tts.save("src/server_src/static/outgoing/" + file_name_output)
#
#
#     # json = ft_action(data['filePath_input'])
#     data['filePath_output'] = file_name_output
#     data['text_output'] = text_output
#
#     json_data = json.dumps(data)
#
#     # return json_data
#     return json_data

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    path = os.getcwd() + '/' + 'src/server_src/static'
    path_incoming = path + '/incoming/'
    path_outgoing = path + '/outgoing/'
    file_name_incoming = str(randrange(1000, 3000)) + str(int(time.time())) + '.wav'
    file_name_outgoing = str(randrange(1000, 3000)) + str(int(time.time())) + '.mp3'
    file_incoming = path_incoming + file_name_incoming
    file_outgoing = path_outgoing + file_name_outgoing
    with open (file_incoming, 'wb') as f:
        f.write(request.data)
        f.close()
    data = {};
    os.system('sox ' + file_incoming + ' -r 16000 ' + path_incoming + 'o_' + file_name_incoming)
    os.system('rm ' + file_incoming)
    output_from_bla = subprocess.check_output('./bla ' + path_incoming + 'o_' + file_name_incoming, shell=True)
    text_output = actionParser(output_from_bla)
    if '(null)' in text_output:
        text_output
    print ('-----------------------------------------------------------\n\n')
    print(output_from_bla)
    print ('-----------------------------------------------------------\n\n')
    data['filePath_input'] = 'o_' + file_name_incoming
    data['text_input'] = output_from_bla
    tts = gTTS(text=text_output, lang='en')
    tts.save(file_outgoing)
    data['filePath_output'] = file_name_outgoing
    data['text_output'] = text_output
    json_data = json.dumps(data)
    return json_data

@app.route('/manual', methods=['GET', 'POST'])
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
            return handler(filename, app.config['UPLOAD_FOLDER'], app.config['OUTGOING_FOLDER'])
    return '''
    <!doctype html>
    <title>KIFT server side</title>
    <h1>Upload wav file</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

def run_the_server(port, path, incoming_folder, outgoing_folder):
    app.config['UPLOAD_FOLDER'] = path + incoming_folder
    app.config['OUTGOING_FOLDER'] = path + outgoing_folder
    app.run(port = port)
