import random

system_random_number = random.randint(1, 100)

while True:
    try:
        user_guess = int(input("Guess the number between 1 to 100: "))
        if user_guess > system_random_number:
            print("Too high!")
        elif user_guess < system_random_number:
            print("Too low!")
        else:
            print("Congratulations! You gussed the number.")
            break
    except ValueError:
        print("Please enter a valid number")
    


