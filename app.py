from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/demo')
def hello_demo():
    return 'Hello from Demo'

@app.route('/demo2')
def hello_again():
    return 'Hello Again'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')