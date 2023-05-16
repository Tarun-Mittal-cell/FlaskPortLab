from flask import Flask
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello!!!!!'

@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs'