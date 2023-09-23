import random

user_guess = int(input("enter a number 1-10: "))


def secret_number():
    random_number = random.randint(1,10)
    return random_number



while True:

    user_guess = int(input("enter a number 1-10: "))



    computer_number = secret_number()
    if user_guess == computer_number:
        print("you guessed it")
        break
        
    elif user_guess > computer_number:
        print("your guess is too high")

    else:
        print("your guess is too low")


