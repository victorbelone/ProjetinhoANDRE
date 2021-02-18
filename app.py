from flask import Flask
from flask import request

def creat_app():
    return Flask(__name__)

app=creat_app()

@app.route('/belone')
def index(): 
    return 'Eai mundo'