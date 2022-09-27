from flask import Flask,request,render_template

from flask_cors import CORS,cross_origin
import os
import json
from Jsonprocessor import ExtractMaxlevels,ExtractData
from json import JSONEncoder
import numpy

from flask_cors import CORS
import os
import json

from flask import Flask,jsonify

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'HR-Allocation-Application')
# template_dir = os.path.join(template_dir, 'frontend')


app = Flask(__name__,template_folder=template_dir)

CORS(app, support_credentials=True)
app.debug=True
# @app.route("/getTest")
# def getData():
#     data ={"id":2,"name":"Anna"}
#     return data
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

@app.route("/teamRequirements",methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def postData():
    
    if request.method == 'POST':
        recvd=request.data#.decode('utf-8')#dict(request.data)
        print("RECV",recvd,"RECV")
        # recvd=b'{"data":{"noOfTeams":1,"numberOfPeople":1,"teamRequirements":[{"type1":"","type2":"","type3":"","type4":"","lvl_type1":"0","lvl_type2":"0","lvl_type3":"0","lvl_type4":"0"}]}}'
        jsonrecvd=json.loads(recvd)
        #response.headers.add('Access-Control-Allow-Origin', '*')
        # print("weeapp.y ",request.data)
       
        result=ExtractMaxlevels(jsonrecvd)
        print("JSON",result,type(result),"JSONRECV")
        # simplified_data = Ext5ractData(jsonrecvd)
        # print(simplified_data)  
        return jsonify(result)
        # return jsonify({"Runing-Live":1})
    else:
        return {"Runing-Live":1}
