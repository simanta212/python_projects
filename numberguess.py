from math import gamma
import random

NUM_LIST = list(range(1,20))

number_picker = random.choice(NUM_LIST)

easy = 10

hard = 5

GAME_TYPE = input("Type 'easy' for easy and 'hard' for hard mode").lower()

if GAME_TYPE == "easy":
    life = easy
if GAME_TYPE == "hard":
    life = hard   


def play_game():
    Tries_left = 0
    
    User_guess = int(input("Guess the number\n"))

    if number_picker < 10 and User_guess > 10:
        print("Too high") 

    elif number_picker > 10 and number_picker < 20 and User_guess > 10 and User_guess < 20:
        print("Too low")

    if User_guess == number_picker:
        print("You guess the correct number") 
    

while life != 0:    
    play_game()
