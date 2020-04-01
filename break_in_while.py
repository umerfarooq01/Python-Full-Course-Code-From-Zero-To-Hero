# In this programe we learn about breack statement in while loop, we use this statement 
# when we want to break our loop on a specfic value or resut.
import random
i=1
while i<=10:
    newR=random.randint(0,20)
    print(newR)
    if newR==6:
        print("Break")
        break
