# Christian Dominic A. Tan
# B.S. Electronics and Communications Engineering
# Electrical and Electronics Engineering Institute
# University of the Philippines Diliman

import pandas as pd

# Replace the first section of the KNN-based MDS Code.py file with this block to perform cleaning on the training dataset
####################################################################################################
training_set = pd.read_csv('training_dataset_allxy.csv')
testing_set = pd.read_csv('testing_dataset_allxy.csv')

training_set_clean = training_set
#print(training_set_clean)

ctr = 0
for row in range(len(training_set)):
    if ctr == 2:    # Number of normal stopped vehicles to remove
        break
    elif training_set.iloc[row, 0] == 0 and training_set.iloc[row, 1] == 0 and training_set.iloc[row, 2] == 0:  # Removes a normal stopped vehicle
        training_set_clean = training_set_clean.drop(row)
        ctr += 1

#print(training_set_clean)

X_train = training_set_clean.iloc[:, 0:2].values    # Use cleaned training_set for X_train and Y_train
Y_train = training_set_clean.iloc[:, 2].values

#X_train = training_set.iloc[:, 0:2].values
#Y_train = training_set.iloc[:, 2].values
X_test = testing_set.iloc[:, 0:2].values
Y_test = testing_set.iloc[:, 2].values

####################################################################################################