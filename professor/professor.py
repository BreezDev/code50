import random

def main():
    # Get the level from the user
    level = get_level()

    # Initialize the score
    score = 0

    # Generate and evaluate 10 math problems
    for _ in range(10):
        # Generate the math problem
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        attempts = 0

        while attempts < 3:
            # Prompt the user for an answer
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

            attempts += 1

        # If the answer was not correct after 3 attempts, show the correct answer
        if attempts == 3 and answer != correct_answer:
            print(f"{x} + {y} = {correct_answer}")

    # Print the final score
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
