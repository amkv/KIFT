import subprocess
from gtts import gTTS
from flask import Flask, make_response
from parser import *
from history import *

def handler(filename, UPLOAD_FOLDER, OUTGOING_FOLDER ):
    try:
        output_from_bla = subprocess.check_output('./bla %(UPLOAD_FOLDER)s/%(filename)s' % {'UPLOAD_FOLDER': UPLOAD_FOLDER, 'filename': filename}, shell=True)
    except:
        output_from_bla = '(null)'
    otgoing_audio = filename + '.mp3'
    output_from_bla = output_from_bla.lower()
    output_from_bla = output_from_bla.strip()
    print ('\n-----------------------------------------------------------\n\n')
    print("'" + output_from_bla + "'")
    print ('-----------------------------------------------------------\n\n')
    text_to_client = actionParser(output_from_bla)
    tts = gTTS(text=text_to_client, lang='en')
    tts.save(OUTGOING_FOLDER + '/' + otgoing_audio)
    response = make_response(open(OUTGOING_FOLDER + '/' + otgoing_audio).read())
    response.headers['Content-Type'] = 'audio/mp3'
    response.headers['Content-Disposition'] = 'attachment; filename=' + otgoing_audio
    path = os.getcwd() + '/' + 'src/server_src/static'
    add_to_history(path, output_from_bla, text_to_client)
    return response
