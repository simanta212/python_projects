import random
value=input("Type the names attending the meal incluiding ,\n")#.lower()
user_pick_options = value.split(", ")

pay = random.choice(user_pick_options)
print(f"{pay} will pay the bill" )
    
