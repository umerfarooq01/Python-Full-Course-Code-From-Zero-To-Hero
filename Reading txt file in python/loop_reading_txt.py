# Here we learn how to read txt file using for loop in python
f=open("month.txt", "r")
for i in f:
    print(i.strip())
