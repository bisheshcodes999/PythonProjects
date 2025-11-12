# Developing a number guessing game for begineers in python
# It shows whether the guesse is too low or too high for the users as well
import random

numbers_guess = random.randint(1, 10)

while True:
    try:
        guess = int(input("Please enter the number you want to guess: "))
        if guess < numbers_guess:
            print("Your guess is too low")
        elif guess > numbers_guess:
            print("Your guess is too high ")
        else:
            print("You guess correct")
            break
    except Exception(ValueError) as e:
        print("Please enter a valid integer for guess between the range ")
