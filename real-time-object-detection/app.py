#!flask/bin/python
from flask import Flask
from libs.fileAccess import *

app = Flask(__name__)

@app.route('/')
def index():
    return libs.fileAccess.readFile("/libs/response.txt")

if __name__ == '__main__':
    app.run(debug=True)
