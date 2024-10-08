def main():
    greeting = input("Enter your greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    # Convert greeting to lowercase for case-insensitive comparison
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
