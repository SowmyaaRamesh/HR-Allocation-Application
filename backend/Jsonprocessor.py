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

    
def ExtractData(jsondata):
    simplified_data = []
    teamRequirements = jsondata["data"]["teamRequirements"]
    for team in teamRequirements:
        data = {
            "sde":0,
            "sdn":0,
            "ne":0,
            "nfit":0
        }
        data[team['type1']] = team['lvl_type1']
        data[team['type2']] = team['lvl_type2']
        data[team['type3']] = team['lvl_type3']
        data[team['type4']] = team['lvl_type4']
        del data[""]
        simplified_data.append(data)
    return simplified_data

data={}
data[""]="hello"
print(data[""])