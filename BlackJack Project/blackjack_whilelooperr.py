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
print(house_total)
   
for total in player:
    player_total > total
    player_total += total
print(player_total)

if player_total > 21 or house_total > 21:
    cards.remove(11)
    cards.append(1)

calculate()

hit = input(f"Please type 'hit' to add a card,or 'n' to cancel\nYour current vard value is {player_total}\n").lower()

player_hit = 0
Player_Three_hit = 0

hit = True
while hit:
    card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    player_hit = random.choice(card)
    print(f"Your card is {player_hit}")
    Player_Three_hit = (player_total +player_hit) 
    print(f"Your pot value is {Player_Three_hit}")
    



if hit=="n":
    hit = False
    print("Result is")

if house_total < player_total:
    print ("You win")
elif house_total > player_total:
    print ("You lost")
elif house_total == player_total:
    
    print ("draw")
else:
    print("Awww error")