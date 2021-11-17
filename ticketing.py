height = (int(input("What is your height 'in cm' \n")))

#photo = (bool())
bill = 0
if height > 120:
    print ("Congrats, you can ride")
    age = (int(input("Enter your age \n")))
    if age < 12:
        bill = 5
    elif  age < 18:
        bill = 7
    else:
        bill = 12

    photo = input("Do you want photo, Y or N \n")

    if photo == "Y" or "y":
        bill += 3
    print(f"Your total bill is {bill}")

else:
    print("Sorry, you are not eligible")

    
              