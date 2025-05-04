import random

secret_number = random.randint(1, 20)

guess = int(input("Try to guess the secret number... "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
        guess = int(input("Try again... "))
    elif guess > secret_number:
        print("Too high")
        guess = int(input("Try again... "))
    

if guess == secret_number:
        print("Congratulations!!!")
#print(guess)
#print(secret_number)
