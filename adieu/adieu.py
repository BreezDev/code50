import sys
import inflect

def main():
    p = inflect.engine()  # Create an inflect engine object
    names = []

    # Prompt the user for names
    print("Enter names, one per line. Press Ctrl-D (or Ctrl-Z on Windows) when done.")
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        # End of input (Ctrl-D or Ctrl-Z)
        pass

    # Use inflect to format the list of names
    if len(names) == 1:
        result = f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        result = f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        formatted_names = ', '.join(names[:-1])  # Join all but the last name with commas
        result = f"Adieu, adieu, to {formatted_names}, and {names[-1]}"

    print(result)

if __name__ == "__main__":
    main()
