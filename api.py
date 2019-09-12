# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 16:10:25 2019

@author: lalit.h.suthar
"""

from _json import make_encoder
from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response
from werkzeug import secure_filename
import json
from json2html import *  # please pip install it
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# to render upload UI
@app.route('/uploads')
def upload():
    return render_template('upload.html')


# to perform file uploads
@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    msg=''
    if request.method == 'POST':
        f = request.files['file']
        f.save("static/data/"+secure_filename(f.filename))
        #cdqa, qag = app1.training()  ### Which will generate final json which contain Q and A it will take at least 20-25 min to generate all question and answers ans saved as Rasa.json
        msg = 'File '+str(f.filename)+' Uploaded Successfully !'
    else:
        msg = 'Upload Failed or Request Failed !'

    return render_template('upload.html', msg=msg)


# to render UI prev
@app.route('/previews')
def preview():
    return render_template('preview.html')


@app.route('/display', methods=['GET', 'POST'])
def display():
    msg = None
    if request.method == "POST":
        fileselect = request.form.get("fileselect", None)

        data = {}
        try:
            if fileselect == "file1":
                data = json.load(open("static/data/Rasa_ppt.json"))

            elif fileselect == "file2":
                data = json.load(open("static/data/Rasa_Word.json"))

            elif str(fileselect).__contains__('--'):
                msg = 'Please Select File !'
                data = {}
            else:
                msg = 'Data for selected file is not available !'

        except Exception:
            msg = 'Data not available'

        #data = jsonify(data)
        #data = json2html.convert(data)
        return render_template('preview.html', msg=msg, data=data)
        #return json_data


@app.route('/about')
def about():
    return render_template('about.html')
	
if __name__ == '__main__':
    app.run(debug=True)