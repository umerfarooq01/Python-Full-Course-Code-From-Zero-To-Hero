# Here we learn about Try... Except Name Error
# In this programe if a Namerror occured in our programe then ou programe tell us that it is NameError outher wise error occurred.
 
try:
    print(y)
except NameError:
    print("NameError Occured") 
except:
    print("Error Occured")   
print("Moving On...")   


# In second programe we divid x/0 so we not that its a math error and our programe tell it is error not nameerror

x=10
try:
    print(x/0)
except NameError:
    print("NameError Occured") 
except:
    print("Error Occured")   
print("Moving On...") 