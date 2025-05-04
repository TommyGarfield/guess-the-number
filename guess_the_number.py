import random

secret_number = random.randint(1, 20)

guess = int(input("Try to guess the secret number... "))

if guess == secret_number:
    print("Congratulations!!!")
elif guess < secret_number:
    print("Too low, try again")
elif guess > secret_number:
    print("Too high, try again")


#print(guess)
#print(secret_number)
