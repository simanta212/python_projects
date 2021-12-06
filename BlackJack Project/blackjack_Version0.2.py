import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

house = random.sample(cards,2)

player = random.sample(cards,2)

house_total = 0
"""bot total count"""
player_total = 0
"""player total count"""

print(house)
print(player)

def calculate():
    """Adds total card count"""

for total in house:
    house_total > total
    house_total += total
# print(house_total)
   
for total in player:
    player_total > total
    player_total += total
# print(player_total)

if player_total > 21 or house_total > 21:
    cards.remove(11)
    cards.append(1)

calculate()
# So the problem was, I placed the user input outside the while-loop. 

player_hit = 0
Player_Three_hit = 0

house_hit = 0
house_three_hit = 0

run = True

hit = input(f"Please type 'hit' to add a card,or 'n' to cancel\nYour card value is {player_total}\n").lower()

if hit == "hit":
    player_hit = random.choice(cards)
    """Player 3rd Hit"""
    print(f"Your card is {player_hit}")
    Player_Three_hit = (player_total + player_hit) 
    print(f"Your pot value is {Player_Three_hit}")
    
    house_hit = random.choice(cards)
    """Bot 3rd Hit"""
    print(f"House card is {house_hit}")
    house_three_hit = (house_total + house_hit )
    print(f"House pot value is {house_three_hit}")
    

if Player_Three_hit > 21:
    print("You lose")
elif player_total==21:
    print("User's BlackJack ")
elif house_total ==21:
    print("house's BlackJack")    
    # if hit=="n":
        # run = False
    
else:
    print(f"current pot value{Player_Three_hit}")
    if house_total < player_total and Player_Three_hit > house_three_hit:
        print ("You win")
    elif house_total > player_total:
        print ("You lost")
    elif house_total == player_total:
        print ("draw")
    else:
        print("Awww error")