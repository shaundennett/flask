from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world  there !"


@app.route('/hello/<name>')
def hello_name(name):
    output_string = "Hello there {0}"
    return output_string.format(name)

if __name__ == '__main__':
    app.run()