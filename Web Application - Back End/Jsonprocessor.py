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
list_of_names=[[[]for i in range(5)]for i in range(len(professions))]#maxlvls NOTEEEEEEE THIS IS ONE BASED INDEXING. 1 to 4
def check(no_of_people):
    ind=-1
    hist=dict()
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        rows=cursor.execute("""SELECT profession, count(profession) FROM employee GROUP BY profession""")
        for proflvl,count in rows:
            hist[proflvl]=count
    # print("hello",no_of_people)
    for p in professions:
        for i in range(1,5):
            var=p+str(i)
            if(hist[var]<no_of_people[ind][i-1]):
                return 0
    # print("weee",hist,"weee")
    ind=-1
    with sqlite3.connect(db_filename) as conn:    
        cursor = conn.cursor()
        for p in professions:
            ind=ind+1
            for i in range(1,5):#lvl
                var=p+str(i)
                rows=cursor.execute("""SELECT  name, id FROM employee WHERE profession=(?) limit (?)""",[var,no_of_people[ind][i-1]])     
                rows=list(rows)
                # print("weeerows",rows[:],"noofp=",no_of_people[ind][i-1],"weee")
                #change available in db       
                for r in rows:
                    name,id =r
                    name=str(id)+'_'+name
                    list_of_names[ind][i].append(tuple([name,var])) #ind is the prof , and i is the lvl
                    # no_of_people[ind][i-1]-=1
                # print("weee",list_of_names[ind]," Prof=",ind,"weee")
                # print(ind,i)
    
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
    list_maxlvls=reqr["teamRequirements"]

    # print(list_maxlvls)
    maxlvls=list()
    for maxlvl_dict in list_maxlvls:
        maxlvl_dict=dict(maxlvl_dict)
        for keys,vals in maxlvl_dict.items():
            if(keys.find("lvl_type")!=-1):
                maxlvls.append(int(vals))
    result=list(predictor(maxlvls)) #the number of people in each prof lvl is returned
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
    print("weee")
    for i in range(len(result)):
        if(i/16==2):
            break
        if(i%16==0):
            print(" ")
        print(result[i],end=" ")
    
    print("weee")
   
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
    #print("weeee no of ppl per lvl, in block profs for all teams",no_of_ppl_perlvl,"weee")
    for p in range(len(no_of_ppl_perlvl)):
        for i in range(len(no_of_ppl_perlvl[p])):
            if(len(list_of_names[p][i+1])!=no_of_ppl_perlvl[p][i]):
                print("error in given and fetch from db")
                # print("wee  P=",p,"I=",i,"weee")
    if(flag==0):
        return {"result":"number of peeople is less"}
    Df_main=[pd.DataFrame(index=range(20)) for i in range(len(Teams))]
    ind=-1
    # print("wee teams ",Teams,"weeee")
    for team in Teams:
        ind=ind+1
        for prof_ind in range(len(team)) :
            prof=team[prof_ind]
            temp=[]
            for lvl in range(max_possible_lvls):
                count=int(prof[lvl])
                # print("Extend: ",list_of_names[prof_ind][lvl][0:count],professions[prof_ind])
                temp.extend(list_of_names[prof_ind][lvl+1][0:count]) #tlist of names is one based
                list_of_names[prof_ind][lvl+1]=list_of_names[prof_ind][lvl+1][count:] #remaining is assigned #one based
            try:
                # print("weeee Team =",ind,"professiion=",prof_ind,temp," weeee ")
                temp=pd.Series(temp)
                # print("weeee Team =",ind,"professiion=",prof_ind,temp," weeee ")
                Df_main[ind][professions[prof_ind]]=temp
                # print(Df_main[ind].head())
                # print(ind,professions[prof_ind])
                temp=[]
            except Exception as e:
                print("Exception: ", temp,e)
    # print("came last")
    path = "../Web Application - Front End/OutputFile/"
    writer = pd.ExcelWriter('pandas_multiple1.xlsx', engine='xlsxwriter')
    Team_sizes=[]
    for i in range(len(Df_main)):
        # print("created")
        # print(Df_main[i].head())
        Df_main[i].to_excel(writer,sheet_name='Team{}'.format(i))
        Team_sizes.append(str(Df_main[i].count().sum()))
    writer.save()
    print("saved")
    RetJson=dict()
    RetJson["status"] ="ok"
    RetJson["data"]=Team_sizes
    return RetJson
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
