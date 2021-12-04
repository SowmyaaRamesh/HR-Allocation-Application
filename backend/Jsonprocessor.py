from ML.ml_predictor import predictor
import json

def ExtractMaxlevels(reqr):
    list_maxlvls=reqr["data"]["teamRequirements"][0]
    maxlvl_dict=dict(list_maxlvls)
    maxlvls=list()
    for keys,vals in maxlvl_dict.items():
        if(keys.find("lvl_type")!=-1):
            maxlvls.append(vals)
    return {"result":list(predictor(maxlvls))}

