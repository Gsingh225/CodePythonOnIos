# app.py
from flask import Flask, request, jsonify, render_template
import subprocess
import sys
import os

app = Flask(__name__)

SAVE_PATH = 'main.py'

if not os.path.exists(SAVE_PATH):
    with open(SAVE_PATH, 'w') as f:
        f.write('print("Hello Ios!")')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load')
def load_file():
    try:
        with open(SAVE_PATH, 'r') as f:
            return f.read()
    except Exception as e:
        return str(e), 500

@app.route('/save', methods=['POST'])
def save_file():
    try:
        code = request.json['code']
        with open(SAVE_PATH, 'w') as f:
            f.write(code)
        return 'OK'
    except Exception as e:
        return str(e), 500

@app.route('/run', methods=['POST'])
def run_code():
    try:
        code = request.json['code']
        # Always save before running
        with open(SAVE_PATH, 'w') as f:
            f.write(code)
        
        result = subprocess.run(
            [sys.executable, SAVE_PATH],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

@app.route('/terminal', methods=['POST'])
def terminal():
    try:
        command = request.json['command']
        allowed_commands = ['pip', 'python', 'python3', 'ls', 'pwd']
        if not any(command.startswith(cmd) for cmd in allowed_commands):
            return "Command not allowed"
        
        result = subprocess.run(
            command.split(),
            capture_output=True,
            text=True,
            timeout=30,
            cwd=os.getcwd()
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
