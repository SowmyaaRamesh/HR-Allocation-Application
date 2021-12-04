#from ML.ml_predictor import predictor
import json

def ExtractMaxlevels(reqr):
    list_maxlvls=reqr["data"]["teamRequirements"]
    print("jacobin",list_maxlvls)
    maxlvl_dict=list_maxlvls[0]
    maxlvls=list()
    for keys,vals in maxlvl_dict:
        if(keys.find("lvl_type")!=-1):
            maxlvls.append(vals)
    return maxlvls

