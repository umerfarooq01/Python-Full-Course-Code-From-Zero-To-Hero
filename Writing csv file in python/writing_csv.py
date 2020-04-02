# Here we learn how to write or append a csv file in python
import csv
updateCsv=["I","Am","Good"]
file=open("example1.csv", "a")
csWriter=csv.writer(file)
csWriter.writerow(updateCsv)
file.closegit 