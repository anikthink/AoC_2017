import csv

with open('02_Input.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    lx = []
    answer = 0
    for row in readCSV:
        for x in range (0, 15):
            a = int(row[x])
            for y in range (0, 15):
                b = int(row[y])
                if (a % b == 0):
                    if (a // b > 1):
                        answer = answer + (a // b)
    print (answer)
