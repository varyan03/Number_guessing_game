import random

#asking the user to enter a number that is greater than 0
range=input("Enter a number")

#checking if its a digit and not 
if range.isdigit():
    range=int(range)

    #checking if the number is less than 0 or not
    if range<=0:
        print("Enter a number greater than 0")
        quit()

    
else :
    print("Only Numerical values accepted ")
    quit()

#generating a random number using random function
random_num=random.randint(0,range)




