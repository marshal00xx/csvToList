import csv
myList = ""
counter = 0
with open('csvFileName.csv') as csv_file:
    # u can set the dilimiter you have in your csv file
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if counter < 10:
            myList += '\"' + str(row[0]) + '\", ' 
file = open('results.txt', 'w')
file.write(myList)
