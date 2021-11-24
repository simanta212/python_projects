def checker(number):
    prime = True
    for  i in range (2, number):
        if number % i == 0 :
            prime = False
    if prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")

number  = int(input("Write the number"))
checker(number)


