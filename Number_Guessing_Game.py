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


#checking if the user has guessed the correct number or not
while True:
    user_guess=input("Guess the number!!")

    #checking if the user has entered the number or not
    if user_guess.isdigit():
        user_guess=int(user_guess)

    else:
        print("Only numeric values accepted")
        continue

    #checking if the user has guessed or not
    if user_guess==random_num:
        print("You got it!!!")
        break

    elif user_guess<random_num:
        print("Enter a greater number.")

    else:
        print("Enter a smaller number")
    
print(random_num)

