import subprocess
from flask import Flask

app = Flask(__name__)

def get_hostname():
    hostname_call = subprocess.run(["hostname", "-i"], stdout=subprocess.DEVNULL)
    return hostname_call.stdout

@app.route('/')
def hello_world():
    return f'Flask Dockerized from {get_hostname()}'

@app.route('/demo')
def demo():
    return f'hello from demo from {get_hostname()}'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
