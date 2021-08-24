from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/getTest")
def getData():
    data ={"id":2,"name":"Anna"}
    return data

@app.route("\postTest"):
def postData():