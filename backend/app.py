from flask import Flask,request,render_template
from flask_cors import CORS
import os
import json
from flask import Request

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'HR-Allocation-Application')
# template_dir = os.path.join(template_dir, 'frontend')

print(template_dir)

app = Flask(__name__,template_folder=template_dir)
CORS(app)

@app.route("/getTest")
def getData():
    data ={"id":2,"name":"Anna"}
    return data

@app.route("/postTest",methods = ['GET', 'POST'])
def postData():
    if request.method == 'POST':
        return request.json