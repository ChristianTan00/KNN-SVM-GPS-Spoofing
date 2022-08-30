import csv
import time

start = time.time()

# Filenames of the training/testing datasets of the individual attacks to combine
a1 = open('testing_dataset_1v.csv','r')
a2 = open('testing_dataset_2v.csv','r')
a4 = open('testing_dataset_4v.csv','r')
a8 = open('testing_dataset_8v.csv','r')
a16 = open('testing_dataset_16v.csv','r')

A1 = list(csv.reader(a1))
A2 = list(csv.reader(a2))
A4 = list(csv.reader(a4))
A8 = list(csv.reader(a8))
A16 = list(csv.reader(a16))

a1.close()
a2.close()
a4.close()
a8.close()
a16.close()

dataset = A1 + A2[1:] + A4[1:] + A8[1:] + A16[1:]

with open('testing_dataset_allv.csv', 'w') as h:        # Filename for the combined training/testing dataset
    writer = csv.writer(h)
    writer.writerows(dataset)

end = time.time()
total_time = time.strftime("%H:%M:%S", time.gmtime(end-start))
print('Execution time:', total_time)