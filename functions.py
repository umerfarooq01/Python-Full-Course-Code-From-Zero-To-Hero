# Creating a Python Function
def hello_fun():
    print("Hello World")

# Calling a Python Function
hello_fun()    

# Passing Arguments to a Function
def hello_func(firstname, lastname):
    print("Hello "+firstname+" "+lastname)

# Calling a Python Function
hello_func("Umer","Farooq")

# Now again create a hello_fun() if user not enter his first name we show a default value or name
def hello_func(firstname="User"):
    print("Hello "+firstname)

# Calling a Python Function
hello_func()

# Creating a function for adding two number
def addNums(arg1,arg2):
    print(arg1+arg2)

# Calling a Python Function
addNums(5,3)       
