from flask.helpers import make_response
from ML.ml_predictor import predictor
import json
import pandas as pd
import sqlite3
from flask import send_file
import io
from pandas.io.excel import ExcelWriter
db_filename = 'hr.db'
professions=["sdn","sde","nfit","ne"]
list_of_names=[[[]for i in range(5)]for i in range(len(professions))]#maxlvls
def check(no_of_people):
    ind=-1
    hist=dict()
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        rows=cursor.execute("""SELECT profession, count(profession) FROM employee GROUP BY profession""")
        for prof,count in rows:
            hist[prof]=count
    print("hello",no_of_people)
    for p in professions:
        for i in range(1,5):
            var=p+str(i)
            if(hist[var]<no_of_people[ind][i-1]):
                return 0
    ind=-1
    with sqlite3.connect(db_filename) as conn:    
        cursor = conn.cursor()
        for p in professions:
            ind=ind+1
            for i in range(1,5):#lvl
                var=p+str(i)
                rows=cursor.execute("""SELECT  name, id FROM employee WHERE profession=(?) limit (?)""",[var,no_of_people[ind][i-1]])     
                rows=list(rows)
                #print(rows[:5])
                #change available in db       
                for r in rows:
                    name,id =r
                    name=str(id)+'_'+name
                    list_of_names[ind][i].append(tuple([name,var])) #ind is the prof , DN I IS THW LVLV
                print(ind,i)
    
    return 1

"""" 1ram  sde1
    2shyam  sde1
    3kam    sde2


req:[sde1:3,sde2:1]
existing:{count(sde1):2, return 0}
req:[sde1:2,sde2:1]
existing:{count(sde1):2,count(sde1):1 return 1}

output:
    list[profession_enum][lvl].append([(1ram,sde1),(2shyam,sde1)])
    
    [[],[],[]] #first lvl abstraction proffesion
    [[[employees in lvl 1 of this profession  ]#(lvl1),[]#(lvl2),[]#(lvl3)] #(sde),[]#(sdn),[]]
input 
csv :a employesert([0:a])   l=l[a:]
es csv[SDE].in
iterate push , break sheet iterate 
[ a: ] , a[]
{
    T1:{
        sde:{
            1:[names]
        }
    }

}
dict["Team1"]["sde"]["lvl"]=[(names)]
list_of_names[index][i].append(tuple(name,var))
"""

            



def ExtractMaxlevels(reqr):
    list_maxlvls=reqr["data"]["teamRequirements"][0]
    maxlvl_dict=dict(list_maxlvls)
    maxlvls=list()
    for keys,vals in maxlvl_dict.items():
        if(keys.find("lvl_type")!=-1):
            maxlvls.append(vals)
    result=list(predictor(maxlvls))
    #
    #extracting using table col formula, instead of getting from list
    Teams=[]
    max_posible_no_teams=10
    maxprofessions=4
    max_possible_lvls=4
    index=0
    teamsize=16
    prof=[]# list of lists consististing a list of lvls for each profession
    temp=[]
    non_zeroteam=0
    no_of_ppl_perlvl=[[0  for i in range(max_possible_lvls)] for i in range(maxprofessions)]
    print(len(result))
   
    for i in range(max_posible_no_teams):
        index=i*teamsize
        prof=[] # will have the team by proffesions
        non_zeroteam=0
        for j in range(0,maxprofessions):
            index=index + int((j!=0))*max_possible_lvls
            temp=[]
            for k in range(0,max_possible_lvls):
                if(result[index+k]>0):
                    non_zeroteam=1
                no_of_ppl_perlvl[j][k]+=result[index+k] #
                temp.append(result[index+k])
            prof.append(temp)
        if(non_zeroteam):
            Teams.append(prof)
    flag=check(no_of_ppl_perlvl)
    if(flag==0):
        return {"result":"number of peeople is less"}
    Df_main=[pd.DataFrame() for i in range(len(Teams))]
    ind=-1

    for team in Teams:
        ind=ind+1
        for prof_ind in range(len(team)) :
            prof=team[prof_ind]
            temp=[]
            for lvl in range(max_possible_lvls):
                count=int(prof[lvl])
                print("Extend: ",list_of_names[prof_ind][lvl][0:count],professions[prof_ind])
                temp.extend(list_of_names[prof_ind][lvl][0:count])
                list_of_names[prof_ind][lvl]=list_of_names[prof_ind][lvl][count:] #remaining is assigned
            try:
                print(temp," in ")
                temp=pd.Series(temp)
                Df_main[ind][professions[prof_ind]]=temp
                print(Df_main[ind].head())
                print(ind,professions[prof_ind])
                temp=[]
            except Exception as e:
                print("Exception: ", temp,e)
    print("came last")
    path = "../frontend/public/assets/"
    writer = pd.ExcelWriter(path+'pandas_multiple.xlsx', engine='xlsxwriter')
    for i in range(len(Df_main)):
        print("created")
        print(Df_main[i].head())
        Df_main[i].to_excel(writer,sheet_name='Team{}'.format(i))
    writer.save()
    return "ok"
    # return send_file(open(path+"pandas_multiple.xlsx",'rb'),attachment_filename="pandas_multiple.xlsx")
    # resp = make_response(file)
    # return resp
    # return 
    # res=make_response(file)
    # return res
    # return {"result":result}
    


        
    
    
                
                    

    

   

    
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

