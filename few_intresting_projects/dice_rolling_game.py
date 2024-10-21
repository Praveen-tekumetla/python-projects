import random


while True:
    choice = input("Roll the Dice? (y/n): ").casefold()

    if choice == 'n':
        print("Thanks for playing!")
        break
    elif choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    else:
        print("Invalid Choice!")
    
 
