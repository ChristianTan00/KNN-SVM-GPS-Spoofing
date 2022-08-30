import pandas as pd
from sklearn.model_selection import train_test_split
import time

start = time.time()
####################################################################################################
attack = [1, 2, 4, 8, 16]        # Attack numbers to use for filenames

for i in attack:
	dataset_r0 = pd.read_csv('dataset_' + str(i) + 'v_r0.csv')        # Filename of repetition #0
	dataset_r1 = pd.read_csv('dataset_' + str(i) + 'v_r1.csv')        # Filename of repetition #1
	dataset_r2 = pd.read_csv('dataset_' + str(i) + 'v_r2.csv')        # Filename of repetition #2
	dataset_r3 = pd.read_csv('dataset_' + str(i) + 'v_r3.csv')        # Filename of repetition #3
	dataset_r4 = pd.read_csv('dataset_' + str(i) + 'v_r4.csv')        # Filename of repetition #4

	train_r0, test_r0 = train_test_split(dataset_r0, test_size = 0.2, random_state = 0)
	train_r1, test_r1 = train_test_split(dataset_r1, test_size = 0.2, random_state = 0)
	train_r2, test_r2 = train_test_split(dataset_r2, test_size = 0.2, random_state = 0)
	train_r3, test_r3 = train_test_split(dataset_r3, test_size = 0.2, random_state = 0)
	train_r4, test_r4 = train_test_split(dataset_r4, test_size = 0.2, random_state = 0)

	training_dataset = pd.concat([train_r0, train_r1, train_r2, train_r3, train_r4], ignore_index = True)
	testing_dataset = pd.concat([test_r0, test_r1, test_r2, test_r3, test_r4], ignore_index = True)

	training_dataset.to_csv('training_dataset_' + str(i) + 'v.csv', encoding = 'utf-8', index = False)        # Filename for training dataset
	testing_dataset.to_csv('testing_dataset_' + str(i) + 'v.csv', encoding = 'utf-8', index = False)          # Filename for testing dataset

####################################################################################################
end = time.time()
total_time = time.strftime("%H:%M:%S", time.gmtime(end-start))
print('Execution time:', total_time)










####################################################################################################
####################################################################################################
""" 	X_r0 = dataset_r0.iloc[:, 0:2]
	Y_r0 = dataset_r0.iloc[:, 2]

	X_r1 = dataset_r1.iloc[:, 0:2]
	Y_r1 = dataset_r1.iloc[:, 2]

	X_r2 = dataset_r2.iloc[:, 0:2]
	Y_r2 = dataset_r2.iloc[:, 2]
	
	X_r3 = dataset_r3.iloc[:, 0:2]
	Y_r3 = dataset_r3.iloc[:, 2]

	X_r4 = dataset_r4.iloc[:, 0:2]
	Y_r4 = dataset_r4.iloc[:, 2] """

""" 	train_r0 = pd.concat([X_train_r0, Y_train_r0], axis = 1)
	test_r0 = pd.concat([X_test_r0, Y_test_r0], axis = 1)

	train_r1 = pd.concat([X_train_r1, Y_train_r1], axis = 1)
	test_r1 = pd.concat([X_test_r1, Y_test_r1], axis = 1)

	train_r2 = pd.concat([X_train_r2, Y_train_r2], axis = 1)
	test_r2 = pd.concat([X_test_r2, Y_test_r2], axis = 1)

	train_r3 = pd.concat([X_train_r3, Y_train_r3], axis = 1)
	test_r3 = pd.concat([X_test_r3, Y_test_r3], axis = 1)

	train_r4 = pd.concat([X_train_r4, Y_train_r4], axis = 1)
	test_r4 = pd.concat([X_test_r4, Y_test_r4], axis = 1) """