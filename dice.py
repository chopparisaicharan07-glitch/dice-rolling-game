import random

print("🎲 Dice Rolling Game")

while True:
    choice = input("\nDo you want to roll the dice? (y/n): ")

    if choice.lower() == "y":
        dice = random.randint(1, 6)
        print("You rolled:", dice)

    elif choice.lower() == "n":
        print("Thanks for playing!")
        break

    else:
        print("Please enter 'y' or 'n'.")