from flask import Flask

server = Flask(__name__)

@server.route('/')
def initalLoad():
    return 'Hello Yuvi'