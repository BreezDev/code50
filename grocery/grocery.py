def main():
    grocery_list = {}

    # Continuously read input until EOFError is encountered
    try:
        while True:
            item = input().strip().lower()
            if item:  # Ignore empty lines
                if item in grocery_list:
                    grocery_list[item] += 1
                else:
                    grocery_list[item] = 1
    except EOFError:
        pass  # End of input

    # Prepare sorted list of items
    sorted_items = sorted(grocery_list.keys())

    # Output results
    for item in sorted_items:
        print(f"{grocery_list[item]} {item.upper()}")

if __name__ == "__main__":
    main()
