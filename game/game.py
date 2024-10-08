import random

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_guess(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    # Get the level from the user
    level = get_positive_integer("Level: ")

    # Generate a random number between 1 and the level (inclusive)
    number = random.randint(1, level)

    # Loop until the user guesses the number correctly
    while True:
        guess = get_guess("Guess: ")

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
