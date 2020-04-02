# We learn how to create sets in python and also learn some methods which is used in python set data type
mySet={"Red","Green","Blue"}
print(mySet)


# Hint >>> we cannot print value as compare to array or list or tuple


# How add some data into our set after creating set
# For example we want to add "Yellow" color into our list 
print(mySet.add("Yellow"))
print(mySet)


# How remove some data into our set after creating set
# For example we want to remove "Yellow" color into our list 
print(mySet.remove("Yellow"))
print(mySet)


# For checking the lenght of python set 
print(len(mySet))


# Now we learn some sets methods (Union, Intersection, Difference)
A={1,2,3,4,5}
B={4,5,6,7,8,9}
# For taking Union of two sets in python
print(A.union(B))


# For taking Intersection of two sets in python
print(A.intersection(B))


# For Checking the Difference of two sets in python

print(A.difference(B))