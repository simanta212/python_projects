from data import data
import random

Guess_data = data
Diplay_city = str(Guess_data)

score = 0

game_continue = True
while game_continue:

    random_date_generate1 = random.choice(Guess_data)
    """Data 1"""
    name_generate = random_date_generate1['name']
    follower_generate = random_date_generate1['follower_count']
    # print(name_generate)
    print(follower_generate)

    random_date_generate2 = random.choice(Guess_data)
    """Data 2"""
    name_generate2 = random_date_generate2['name']
    follower_generate2 = random_date_generate2['follower_count']
    # print(name_generate2)
    print(follower_generate2)
    # # print(data)

    print(f"Who has more followers?\n {name_generate} vs {name_generate2}")
    user_guess = int(input(f"Please type 1 for {name_generate} and 2 for {name_generate2} "))


    # This also works
    # if user_guess == 1:
    #     if follower_generate > follower_generate2:
    #         print ("you win")
    #     if follower_generate2 > follower_generate:
    #         print ("you lose")
    # if user_guess == 2:
    #     if  follower_generate > follower_generate2:
    #         print ("You lose")
    #     if  follower_generate2 > follower_generate:
    #         print ("You win")

    if user_guess == 1 and follower_generate > follower_generate2:
        print("You win")
        score +=1
    elif user_guess == 2 and follower_generate < follower_generate2:
        print("you win")
        score +=1
    else: 
        print("you lost")
        print(f"final score{score}")
        game_continue = False

    