from flask import Flask,request,render_template
from flask_cors import CORS
import os
import json
from Jsonprocessor import ExtractMaxlevels


template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'HR-Allocation-Application')
# template_dir = os.path.join(template_dir, 'frontend')

print(template_dir)

app = Flask(__name__,template_folder=template_dir)
CORS(app)

# @app.route("/getTest")
# def getData():
#     data ={"id":2,"name":"Anna"}
#     return data

@app.route("/teamRequirements",methods = ['GET', 'POST'])
def postData():
    if request.method == 'POST':

        recvd=request.data.decode('utf-8')#dict(request.data)
        jsonrecvd=json.loads(recvd)
        return json.dumps({"ans":ExtractMaxlevels(jsonrecvd)})
    else:
        return {"sucess":1}
