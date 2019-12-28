import os
import uuid

from flask import (
    render_template,
    make_response,
    request,
    send_file,
    jsonify,
)

from app import app
from app.converter import Converter


@app.route('/', methods=['POST', 'GET'])
def upload():
    return render_template('index.html')


@app.route("/getfile", methods=["POST"])
def getfile():
    fileob = request.files["file"]
    if fileob.filename.split('.')[-1] != 'wav':
        return 'WAV only!', 400

    filename = fileob.name

    response = jsonify(filename=filename)
    return make_response(response, 201)


@app.route("/convert", methods=["POST"])
def convert():
    pass
