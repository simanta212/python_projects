run_again = True
while run_again:
    a = int(input("Enter the number 'a' "))
    b = int(input("Enter the number 'b' "))

    c = a + b
    print(f"The sum of a and b is:{c} \n")
    user_choice = input("You want to run the program again ? 'Y' for yes and 'N' for no.\n").lower()
    if user_choice == "n":
        run_again = False
        print("The program is closed.")