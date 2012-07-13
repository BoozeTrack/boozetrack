from booze import app
from flask import render_template
from flask import jsonify

import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        pass

@app.route('/env')
def env():
    return jsonify(os.environ)
