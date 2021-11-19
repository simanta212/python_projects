import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("what do u want to choose 0 = rock, 1 = paper, 2 = scissor\n"))
if user_choice <=3:
    print(game_images[user_choice])

    bot_choice =int(random.randint(0,2))
    print(f"bot choosed \n{game_images[bot_choice]}")
    
    if user_choice == bot_choice:
        print("It's a draw")
    elif user_choice == 0 and  bot_choice == 1:
        print("You lost")  
    elif user_choice == 1 and bot_choice == 0:
        print("You win")  
    elif user_choice == 2 and   bot_choice == 0:
        print("you lost")
    elif user_choice == 1 and bot_choice == 2:
        print ("You lost")    
    else:
        print("you win")
else:
    print("you didn't choosed correct value")
