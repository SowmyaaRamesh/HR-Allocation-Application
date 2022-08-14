This folder contains:
1. Sample dataset depicting the calculation of probability impact and HR scores
2. Synthetic dataset for training a suitable regression model
3. Code for generating the dataset
4. Code for the decision tree-based regression model 

The data set contains 100,000 rows and 320 columns. The first 160 columns contain the probability impact values. The rationale behind having 160 columns for this is as follows:
There are a maximum of 10 teams. Each team has a maximum of 4 different classes of employees. Each employee class has a maximum of 4 levels. Hence, there are 4x4x10=160 columns.
The next 160 columns in the dataset contain the HR score corresponding to the previous 160. The HR score is computed according to a staircase function.
