# Christian Dominic A. Tan
# B.S. Electronics and Communications Engineering
# Electrical and Electronics Engineering Institute
# University of the Philippines Diliman

import pandas as pd
import time

start = time.time()
####################################################################################################
training_set = pd.read_csv('training_dataset_1v.csv')		# Filename of training set
testing_set = pd.read_csv('testing_dataset_1v.csv')		# Filename of testing set

X_train = training_set.iloc[:, 0:2].values
Y_train = training_set.iloc[:, 2].values
X_test = testing_set.iloc[:, 0:2].values
Y_test = testing_set.iloc[:, 2].values

####################################################################################################
from sklearn.neighbors import KNeighborsClassifier		# Uncomment block below to perform hyperparameter tuning/cross-validation
""" clf2 = KNeighborsClassifier()
hyperparameter = {'n_neighbors': list(range(1, 101))}

from sklearn.model_selection import RandomizedSearchCV
randomized_search = RandomizedSearchCV(estimator = clf2, param_distributions = hyperparameter, verbose = 1, n_jobs = -1, n_iter = 100)
randomized_result = randomized_search.fit(X_train, Y_train)
print('Best Score:', randomized_result.best_score_)
print('Best Hyperparameter:', randomized_result.best_params_) """

####################################################################################################
#k = randomized_result.best_params_['n_neighbors']		# Uncomment if hyperparameter tuning block is uncommented
k = 6													# Comment out if hyperparameter tuning block is uncommented
clf = KNeighborsClassifier(n_neighbors = k)
clf.fit(X_train, Y_train)

training_accuracy = clf.score(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)
print('\nTraining accuracy of KNN with k =', k, 'for the given datasets:', round(training_accuracy, 4))
print('Accuracy of KNN with k =', k, 'for the given datasets:', round(accuracy, 4))

####################################################################################################
from sklearn.metrics import precision_score, recall_score, f1_score
Y_pred = clf.predict(X_test)
print('Precision =', round(precision_score(Y_test, Y_pred), 4))
print('Recall =', round(recall_score(Y_test, Y_pred), 4))
print('F1-score =', round(f1_score(Y_test, Y_pred), 4))

####################################################################################################
end = time.time()
total_time = time.strftime("%H:%M:%S", time.gmtime(end-start))
print('Execution time:', total_time)