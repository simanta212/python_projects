import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

house = random.sample(cards,2)
player = random.sample(cards,2)

player_total = 0

def add():
    house_total = 0
    for total in house:
        house_total > total
        house_total += total
    print(house_total)



print(house, player)
add()