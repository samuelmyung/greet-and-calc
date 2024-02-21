# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get('/add')
def addition():
    "Handles get requests for addition with two parameters"
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a,b))

@app.get('/sub')
def subtraction():
    "Handles get requests for subtraction with two parameters"
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(sub(a, b))

@app.get('/mult')
def multiplication():
    "Handles get requests for multiplication with two parameters"
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(mult(a, b))

@app.get('/div')
def division():
    "Handles get requests for division with two parameters"
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(div(a, b))
