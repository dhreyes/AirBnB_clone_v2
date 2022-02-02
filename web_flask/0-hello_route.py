#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
The web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
Must use the option strict_slashes=False in route definition
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'