user_age    =   int(input())
#user_age_conerter = int(user_age)

x = 90 - user_age #age left in years
y = x * 365       #age left in days
z = y / 30        #age left in months
a = y / 52        #age left in weeks   
    
print(f"age in years left {x},\nage in days left {y},\nage in months left {z},\nage in weeks left {a}")


