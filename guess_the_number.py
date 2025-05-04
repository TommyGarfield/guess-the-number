import random

#storing random number in secret_number
secret_number = random.randint(1, 20)

#asks user for number
guess = int(input("Try to guess the secret number... "))

#if number too high or low ask them to try again
while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
        guess = int(input("Try again... "))
    elif guess > secret_number:
        print("Too high")
        guess = int(input("Try again... "))
    

#prints message when guess is correct
print("Congratulations, thats the number!!!")

        
#print(guess)
#print(secret_number)
