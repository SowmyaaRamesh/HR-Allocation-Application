import random


def random_team_number(): #Number of teams
  return random.randint(1,10)

def random_engg_levels(): # list of levels in each profession(const  4 professions) [ 4*teamsize]
  teams = random_team_number()
  max_levels = []
  for i in range(teams):
    for j in range(4):
      max_levels.append(random.randint(0,4))  #ddoubt do we need 0? is that a way to reduce a profession?
  for i in range(10-teams):
    for j in range(4):
      max_levels.append(0)     #doubt illa, still this is for team selction part
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
              for levels in range(4): #doubt isn;t it supposed to be range()
                fill = random.choices([0,1],weights=(95,5),k=1)[0] #decides whether the profession of tht level exists
                if(fill and (sum(probability_impact)<1)):
                    if(sum(probability_impact)<0.7):
                        probability_impact.append(get_random_value())   
                    else:
                        probability_impact.append(round(1 - sum(probability_impact),1))
                else:
                    probability_impact.append(0.0)
        if sum(probability_impact)!=1: 
          zeros_list = []
          for i in range(len(probability_impact)): #doubt, prob can come when the team doent need to exist, so the below random cld be reducced to a range?
            if probability_impact[i]==0: zeros_list.append(i)
          probability_impact[random.choice(zeros_list)] = round(1-sum(probability_impact),1)
        responsibility_matrix.append(probability_impact)
    return responsibility_matrix

l = random_engg_levels()
print(l)
ans = generate_responsibility_matrix(l)
for i in ans:
  print(len(i),sum(i))
probability_impact_row = []
for col in range(160): probability_impact_row.append(round(sum(row[col] for row in ans),1)) #the last row probability impact is the maount of contribution of that lvl fot all 8 chaallenges


print(len(ans),"*",len(ans[0]))