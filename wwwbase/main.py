# coding: utf-8
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import os
import json
app = Flask(__name__)

@app.route('/_rnn_check')
def add_numbers():
    contents = request.args.get('contents', "", type=str)
    res = os.popen('echo "' + contents + '" | p3 ../chainer-term-rnn/ConditionalRandomField.py').read()
    return jsonify(result=json.loads(res))

@app.route("/")
def hello():
    return render_template("index.html", title="PROOFREADING")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
