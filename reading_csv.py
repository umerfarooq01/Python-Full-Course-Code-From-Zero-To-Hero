# Here we learn how to read a csv file in python
import csv
file = open ("example1.csv", "r")
csReader=csv.reader(file, delimiter=",")
for row in csReader:
    print(row)
file.close()    