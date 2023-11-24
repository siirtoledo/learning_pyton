import random


targetNum=random.randint(1,10)

attempts= 0


while attempts < 4:
    userInput=int(input("Please guess a number: "))
    
    if  userInput < targetNum:
        print("Sorry number is too low. Try again")
    elif userInput > targetNum:
        print("Sorry number is too high try again")
    else:
        print("Awesome you guessed the right number")
    attempts+=1
    
    


