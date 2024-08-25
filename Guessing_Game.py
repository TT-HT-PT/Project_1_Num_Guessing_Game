# This imports the random module from the python library
import random
           
# Import the random function from the random module

print("Welcome to 'Guess the right number' ")
attempts = 1
first_play = 0
print("Current high score is",first_play)
# Run the following code when the user input is not the same as the random number 
def start_game():
    user_num = 0
    rand_num = random.randrange(1,10)
    global attempts
    while user_num is not rand_num:
        # Check for the exceptions in the user input
        try:
            user_num = int(input("Input any number between 1 to 10: "))
            if user_num <= 0:
                print("You entered a negative number. Please use a positive number between 1 and 10: ")
                attempts += 1
            elif user_num > 10:
                print("You entered a number that is outside the range provide. Please enter a number between 1 to 10: ")
                attempts += 1
            elif user_num > rand_num:
                print("You guessed a higher number. Please try again")
                attempts += 1       
            elif user_num < rand_num:
                print("You guessed a lower number. Please try again")
                attempts += 1
            else:
                print("You guessed it right. It took you {} attempt/s to guess it correctly! Great job!".format(attempts))
                high_score = attempts       
                def re_play():
                    choice = input("Do you want to play again? Yes/No ") 
                    if choice.lower() == "yes":
                        print("Current High Score is",high_score)
                        start_game()
                    elif choice.lower() == "no": 
                        print("Thank you for playing. You played well!") 
                    else:
                        print("That was an invalid input. Please enter Yes or No")
                        re_play()
                re_play()
        except ValueError:
                print("You entered a non numerical value. Please enter a Numercial value between 1 to 10")
                   
start_game()
  

