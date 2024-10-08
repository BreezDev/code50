import sys
import random
from pyfiglet import Figlet

def print_usage_and_exit(message):
    print(message)
    sys.exit(1)  # Exit with non-zero status code

def main():
    figlet = Figlet()

    # Handle command-line arguments
    if len(sys.argv) == 1:
        # No font specified; use a random font
        fonts = figlet.getFonts()
        font = random.choice(fonts)
        figlet.setFont(font=font)
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        # Font specified; validate the font
        font = sys.argv[2]
        fonts = figlet.getFonts()
        if font not in fonts:
            print_usage_and_exit("Invalid usage")
        figlet.setFont(font=font)
    else:
        # Invalid command-line arguments
        print_usage_and_exit("Invalid usage")

    # Prompt the user for text
    text = input()

    # Render and print the text in the selected font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
