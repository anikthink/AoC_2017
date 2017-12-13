import csv
with open('04_Input.csv') as csvfile:
    incorrect = 0
    correct = 0
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
        for i in row:
            for j in row:
                if i == j:
                    incorrect = incorrect + 1
                break
        correct = correct + 1
    print (incorrect)
    print (correct)
