import pandas as pd

import time
start = time.time()

from sklearn.model_selection import train_test_split
training_set = pd.read_csv("traininga.csv") ##filename for training set
test_set = pd.read_csv("testinga.csv")      ##filename for testing set

X_train = training_set.iloc[:,0:2].values
Y_train = training_set.iloc[:,2].values
X_test = test_set.iloc[:,0:2].values
Y_test = test_set.iloc[:,2].values

from sklearn.svm import SVC
classifier = SVC(C=100,gamma=10, kernel='rbf', random_state = 1)
classifier.fit(X_train,Y_train)

end = time.time()
total = time.strftime("%H:%M:%S", time.gmtime(end-start))
print("Fit Finished:",total)

Y_pred = classifier.predict(X_test)

print("Combined:\n")

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test,Y_pred)
accuracy = float(cm.diagonal().sum())/len(Y_test)
print("Accuracy Of SVM For The Given Dataset : ", accuracy)

from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score
print("precision:" , precision_score(Y_test,Y_pred))
print("recall:" , recall_score(Y_test,Y_pred))
print("f1 score :" , f1_score(Y_test,Y_pred))
print("accuracy:" , accuracy_score(Y_test,Y_pred))


end = time.time()
total = time.strftime("%H:%M:%S", time.gmtime(end-start))
print("\nDuration:",total)
