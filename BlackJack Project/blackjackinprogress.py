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

if house_total < player_total:
    print ("You win")
elif house_total > player_total:
    print ("You lost")
elif house_total == player_total:
    
    print ("draw")
else:
    print("Awww error")

