import random

Vault = ["milk","silk","dead" ]

word_randomaization = random.choice(Vault)

user_guess = input("Guess the letter").lower()

print(f"The word was {word_randomaization} ")

for word in word_randomaization:
    if word == user_guess:
        print("solved")
    else:
        print("unsoved")
