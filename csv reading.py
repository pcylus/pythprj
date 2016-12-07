import sys
import csv

with open('file.csv', 'r') as f:
    reader = csv.reader(f, delimiter = ',')
    print(reader)
    for x in reader:
        for y in x:
            print(y[2])