

# 1) Number Guessing Game

import random 

computer = random.randint(1, 100)    #pick random number between 1 to 100
 

attempt = 0   # set variable (Attempt) to 0

while True:
    try:
        user= int(input("Enter a number between 1 - 100 : "))     # Take integer as input from user

        attempt = attempt + 1       # everytime user give input, attempt will be increase by 1

        if (user > computer):
            print("Your guess is higher ")
            
        elif (user < computer):
            print("Your guess is Lower ")
            
        else:
            print(f"Your guess is correct i.e User: {user} = Computer:  {computer} ")
            print(f"You guessed it right in {attempt} attempt")

            decision = input("Do you want to play again? (y/n): ")       # Ask if user want to continue
            attempt = 0                                                 # Reset Attempt
            if (decision == 'n' or decision == 'N' ):                   #if user don't want to play, program will end
                print("---End Game---")
                break
    except ValueError as e:                           #if user give input aside from integer, run print statement and again ask
        print("---Enter number only !! ---")


    

        


