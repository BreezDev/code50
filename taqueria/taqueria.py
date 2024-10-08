def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.0

    print("Enter items (Ctrl-D to finish):")

    while True:
        try:
            item = input("Item: ").strip()
            normalized_item = item.title()

            if normalized_item in menu:
                total += menu[normalized_item]

            print(f"Total: ${total:.2f}")

        except EOFError:
            print()  # Print a new line before exiting
            break

if __name__ == "__main__":
    main()
