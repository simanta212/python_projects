

run = True
while run:
    amount = [1, 3, 5, 11, 5, 10, 7]
    sum = 0
    top = 0
    for i in amount:
        i > sum
        sum += i
        if i > top:
            top = i
    print(sum)
    print(top)

    retry = input("You wish to rerun the program ? 'Y' for yes and 'N' for no.\n").lower()

    if retry == "n":
        run = False
        print("Closed")

