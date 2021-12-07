from math import gamma
import random

NUM_LIST = list(range(1,100))

number_picker = random.choice(NUM_LIST)

easy = 10

hard = 5

GAME_TYPE = input("Type 'easy' for easy and 'hard' for hard mode").lower()

if GAME_TYPE == "easy":
    life = easy
if GAME_TYPE == "hard":
    life = hard   


def play_game():
    User_guess = int(input("Guess the number\n"))
    
    if User_guess == number_picker:
        print("You guess the correct number") 

while life != 0:    
    play_game()
