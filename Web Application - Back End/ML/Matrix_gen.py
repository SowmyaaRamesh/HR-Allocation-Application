import random


def random_team_number(): #Number of teams
  return random.randint(1,10)

def random_engg_levels(): # list of levels in each profession(const  4 professions) [ 4*teamsize]
  teams = random_team_number()
  max_levels = []
  for i in range(teams):
    for j in range(4):
      max_levels.append(random.randint(0,4))  #ddoubt do we need 0? is that a way to reduce a profession?
  return max_levels

def get_random_value():
  value_list = [0.1,0.2,0.3]
  random_value = random.choices(value_list,weights=(40,40,20),k=1)
  return random_value[0]


def generate_responsibility_matrix(max_levels):
    responsibility_matrix = []
    for challenges in range(0,8):
        probability_impact = []
        for max_level in max_levels:
            if max_level==0:
              for levels in range(4):
                probability_impact.append(0.0)
            else:
              for levels in range(4):
                if(levels < max_level):
                  fill = random.choices([0,1],weights=(95,5),k=1)[0]
                  if(fill and (sum(probability_impact)<1)):
                      if(sum(probability_impact)<0.7):
                          probability_impact.append(get_random_value())   
                      else:
                          probability_impact.append(round(0.9 - sum(probability_impact),1))
                  else:
                      probability_impact.append(0.0)
                else:
                      probability_impact.append(0.0)
        if sum(probability_impact)!=1:
          choice_list = []
          for i in range(len(probability_impact)):
            if probability_impact[i]!=0: choice_list.append(i)
          if len(choice_list)==0: random_num = 4
          else: random_num = random.choice(choice_list)
          probability_impact[random_num] += round(0.9-sum(probability_impact),1)   
        responsibility_matrix.append(probability_impact)
    return responsibility_matrix

# l = random_engg_levels()
# print(l)
# ans = generate_responsibility_matrix(l)
# for i in ans:
#   print(len(i),sum(i))
# probability_impact_row = []
# for col in range(160): probability_impact_row.append(round(sum(row[col] for row in ans),1)) #the last row probability impact is the maount of contribution of that lvl fot all 8 chaallenges

def pad(responsibility_matrix,teams):
  ret_resp_mat = []
  for i in responsibility_matrix: 
    i+= [0 for i in range(16*(10-teams))]
    ret_resp_mat.append(i)
  return ret_resp_mat

def percent_to_hr(probability_impact_row):
  hr_list = []
  for frac in probability_impact_row: 
    i = (frac/8.0)*100
    if i >= 42: hr_list.append(6)
    elif i>=36 and i<42: hr_list.append(5)
    elif i>=30 and i<36: hr_list.append(4)
    elif i>=24 and i<30: hr_list.append(3)
    elif i>=20 and i<24: hr_list.append(2)
    elif i>0 and i<20: hr_list.append(1)
    else: hr_list.append(0)
  return hr_list

def gen_probability_impact_row(responsibility_matrix,teams):
  responsibility_matrix  = pad(responsibility_matrix,teams)
  #for i in responsibility_matrix: print(len(i),sum(i))
  probability_impact_row = []
  # print("EEEEEEEEEEEEEEEEe",len(responsibility_matrix[0]))
  for col in range(160): 
    probability_impact_row.append(round(sum(row[col] for row in responsibility_matrix),1))
  for i in range(0,16*teams,16):
    probability_impact_row[i] += 0.1
  return probability_impact_row


# probability_impact_list = []
# for rows in range(100000):
#   l = random_engg_levels()
#   responsibility_matrix = generate_responsibility_matrix(l)
#   probability_impact_row = []
#   for col in range(160): probability_impact_row.append(round(sum(row[col] for row in responsibility_matrix),1))
#   hr_row = percent_to_hr(probability_impact_row)
#   dataframe_row = probability_impact_row + hr_row
#   probability_impact_list.append(dataframe_row)


