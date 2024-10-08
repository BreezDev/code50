def main():
    # Define the list of month names
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        # Print a prompt message for the user
        print("Enter a date (MM/DD/YYYY or Month DD, YYYY):", end="")

        try:
            date_input = input().strip()

            # Try to parse the MM/DD/YYYY format
            try:
                month, day, year = map(int, date_input.split('/'))
                if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
                    # Format and output in YYYY-MM-DD
                    print(f"{year:04}-{month:02}-{day:02}")
                    return
            except ValueError:
                pass  # Continue to try the next format if this fails

            # Try to parse the Month DD, YYYY format
            try:
                month_name, day_year = date_input.split(' ', 1)
                day, year = day_year.split(', ')
                day = int(day)
                year = int(year)
                month = months.index(month_name) + 1
                if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
                    # Format and output in YYYY-MM-DD
                    print(f"{year:04}-{month:02}-{day:02}")
                    return
            except (ValueError, IndexError):
                pass  # Continue if parsing fails

            # If neither format was valid, prompt again
            print("Invalid date format. Please try again.")

        except EOFError:
            break

if __name__ == "__main__":
    main()
