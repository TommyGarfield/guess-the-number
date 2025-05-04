import random

#storing random number in secret_number
secret_number = random.randint(1, 20)

#created a guess counter
counter = 0

#asks user for number
guess = int(input("Try to guess the secret number... "))
#adds 1 to the counter after first guess
counter += 1


#if number too high or low ask them to try again,
#adds 1 to the guess counter each time
while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
       
    elif guess > secret_number:
        print("Too high")

    guess = int(input("Try again... "))
    counter += 1
    
        

#prints message when guess is correct
print("Congratulations, thats the number!!! It took you",counter, "guesses!")

