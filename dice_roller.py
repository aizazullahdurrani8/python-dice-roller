import random  # Used for generating random numbers

def roll_dice(sides=6, rolls=1):
    """
    Rolls a die with the specified number of sides, multiple times.
    
    Parameters:
    - sides (int): Number of sides on the die (default is 6)
    - rolls (int): Number of times to roll the die
    
    Returns:
    - List of integers representing the results of each roll
    """
    # Generate a list of random integers for each roll
    results = [random.randint(1, sides) for _ in range(rolls)]
    return results

def main():
    print("Dice Roller")

    try:
        # Ask user for number of sides (e.g., 6 for standard die)
        sides = int(input("Enter number of sides on the die (default 6): ") or 6)

        # Ask user how many times to roll the die
        rolls = int(input("How many times to roll? (default 1): ") or 1)
    except ValueError:
        # Handle invalid (non-integer) input
        print("Please enter valid numbers.")
        return

    # Perform the dice rolls
    results = roll_dice(sides, rolls)

    # Display the results to the user
    for i, result in enumerate(results, 1):
        print(f"Roll {i}: {result}")

# Entry point of the script
if __name__ == "__main__":
    main()
