from math import gamma
import random

NUM_LIST = list(range(1,50))

number_picker = random.choice(NUM_LIST)

#easy = 10

#hard = 5

game_type = input("Type 'easy' for easy and 'hard' for hard mode\n").lower()
#life = 0   
if game_type == "easy":
        life = 10
if  game_type == "hard":
        life = 5
game_finished = False

while not game_finished :
    User_guess = int(input("Guess the number\n"))
    
    
        #if number_picker < 10 and User_guess > 10:
    if number_picker > User_guess:
        print("Too low") 
        life -= 1
        #elif number_picker > 10 and number_picker < 20 and User_guess < 10 and User_guess > 20:
    elif number_picker < User_guess:
        print("Too high")
        life -= 1
    elif User_guess == number_picker:
        print("You guess the correct number") 
    
    print(f"Your have {life} try left")
    
    if life == 0:
        game_finished = True
        print("retry")

