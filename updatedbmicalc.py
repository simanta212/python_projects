print("weight in 'KGs'\n")

weight = float(input())

print("height in 'feet'\n")

height = float(input())

#converted user height from feet to meter where 1 meter= 3.28 feet

User_height_convert = height/3.28


bmi = weight/(User_height_convert*User_height_convert)
 

value = round(bmi, 2)

print(type(value))

print(f"Your bmi is {value}\n")

#-------------- problem lies below, variable named value has user bmi stored as float but no matter how much is ur bmi, always else statement is executed. Is my ifelse statement thinks the variable value is a string. Then why is it not showing correct output.Thankyou for your time ----------------

if value < 18.5:

    print("You are underweight, eat more bud")

elif  value < 24.9:

    print("You are healthy")

elif value < 29.9:

    print("you are overweight please do some exercise")

elif value < 34.9:

    print("Obese")

else:
    print("extreme Obese")