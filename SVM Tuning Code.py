import pandas as pd
import numpy as np
from sklearn.metrics import make_scorer, roc_auc_score
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV 

import time
start = time.time()


training_set = pd.read_csv("validationa_r0.csv") ##filename for training set

X_train = training_set.iloc[:,0:2].values
Y_train = training_set.iloc[:,2].values

 
# DEFINE MODEL AND PERFORMANCE MEASURE
mdl = SVC(probability = True, random_state = 1)
auc = make_scorer(roc_auc_score)

rand_list = {"C": np.logspace(-1, 2, 4),
             "gamma": np.logspace(-4,1,6)}
              
rand_search = RandomizedSearchCV(mdl, param_distributions = rand_list, n_iter = 20, random_state = 2017, scoring = auc) 
rand_search.fit(X_train, Y_train) 
print(rand_search.cv_results_)

print(
    "The best parameters are %s with a score of %0.2f"
    % (rand_search.best_params_, rand_search.best_score_)
)

end = time.time()
total = time.strftime("%H:%M:%S", time.gmtime(end-start))
print(total)
