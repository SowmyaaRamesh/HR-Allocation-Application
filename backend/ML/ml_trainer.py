from .Matrix_gen import *
import pandas as pd
from numpy import absolute
from numpy import mean
from numpy import std
import pickle
from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
# hr_df = pd.DataFrame(probability_impact_list)
# hr_df.to_csv('hrdetails.csv')
import os




def trainer():
    df = pd.read_csv(filepath_or_buffer='hrdetails.csv',index_col=0)
    df.columns=[i for i in range(1,321)]
    df.head()
    X = df[[i for i in range(1,161)]]
    y = df[[i for i in range(161,321)]]
    y.columns=[[i for i in range(1,161)]]
    model = DecisionTreeRegressor() #doubt thikn descision tree is not the ryt one, since y is supposed to be a single number and not list
    #cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
    #n_scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
    #n_scores = absolute(n_scores)
    #print('MAE: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(files,"is not in ",os.curdir)
    if("model1" not in files):
        model.fit(X, y)
        pickle.dump(model, open("model1",'wb'))
    else:
        model = pickle.load(open("model1",'rb'))
    return model #doubt would pickling it work , since training model takes less time we can use this
    #doubt instead of returning the trained modek , we can pikle it as a file

