user1 = input("Ener your name\n")
user2 = input("Enter your 'partner / crush' name\n")

sumed_strings = user1 + user2

lowered_char =  sumed_strings.lower()

t = lowered_char.count("t")
r=lowered_char.count("r")
u=lowered_char.count("u")
e=lowered_char.count("e")

true = t + r + u + e

l=lowered_char.count("l")
o=lowered_char.count("o")
v=lowered_char.count("v")
e=lowered_char.count("e")

love = l + o + v + e

couple_score = str(true)+ str(love)
print(f"love score {couple_score}")

if int(couple_score) < 10:
    print("You guys are like north pole and south pole")
elif int(couple_score) < 20:
    print("You are ok together")    
else:
    print("Made for each other")