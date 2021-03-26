from flask import Flask,request, Response
import json

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route('/hello')
def homepage():
    response = {"message": "Hello World"}
    return 'Welcome to my page'

if __name__ == '__main__':
    FLASK_DEBUG = True
    app.run()