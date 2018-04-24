import csv

with open('Flo.csv') as file:
    reader = csv.reader(file, delimiter = '')

    count =0

    for row in reader:
        print (row [9])

        if count > 100 :
            break

        count += 1
