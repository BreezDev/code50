def main():
    while True:
        try:
            # Prompt user for a fraction
            fraction = input("Fraction: ").strip()
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            # Validate denominator
            if y == 0:
                raise ZeroDivisionError

            # Validate fraction values
            if x > y:
                raise ValueError

            # Calculate percentage
            percentage = round((x / y) * 100)

            # Determine output
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()
