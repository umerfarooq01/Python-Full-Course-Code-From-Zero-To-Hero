# Now we learn how to create and append a list in python.
# Remember we use these brackets[] in list 
myList=["Red","Green","Blue"]


# For printing whole list
print(myList)


# Now we know that python list or array is zero based and list value start from 0 to n
#example myList[0]=Red
print(myList[0])
print(myList[1])
print(myList[2])


#Now we learn how to append or add some list items after creating list
# now we want to add yellow color in our list 
print(myList.append("Yellow"))


# Yellow is added in myList
print(myList)


#Now we learn how to reomve some list items after creating list
# now we want to remove yellow color in our list 
print(myList.remove("Yellow"))


# Yellow is removed in myList
print(myList)


# For checking the lenght of list items
print(len(myList))


# For reversing the list items
print(myList.reverse())
print(myList)


# Another method of printing List (List Constructor)
Awsomelist=list(("Red","Green","Blue"))
print(Awsomelist)


# For removing or clear list in python
print(Awsomelist.clear())
