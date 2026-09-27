import random

print("🎲 Dice Rolling Game")

while True:
    choice = input("\nDo you want to roll the dice? (y/n): ")

    if choice.lower() == "y":
        dice = random.randint(1, 6)
        print("You rolled:", dice)

        # Store result in file
        with open("dice_results.txt", "a") as file:
            file.write(f"You rolled: {dice}\n")

    elif choice.lower() == "n":
        print("Thanks for playing!")
        break

    else:
        print("Please enter 'y' or 'n'.")

# Read the file
print("\n📄 Previous Dice Results:")

with open("dice_results.txt", "r") as file:
    results = file.read()

print(results)
