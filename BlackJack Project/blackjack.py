import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

house = random.sample(cards,2)
player = random.sample(cards,2)

def sum_house():
    """Adds total card count"""
    house_total = 0
    for total in house:
        house_total > total
        house_total += total
    print(house_total)

def sum_player():
    """Adds total card count of player"""
    player_total = 0
    for total in player:
        player_total > total
        player_total += total
    print(player_total)


print(house, player)
sum_house()
sum_player()

val1=0
"""house score"""
val2=0
"""player score"""

sum_house==val1
sum_player==val2
if val1 > val2:
    print("You won")
else:
    print("you lose")