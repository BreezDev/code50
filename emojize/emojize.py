import emoji

def main():
    # Prompt the user for input
    user_input = input("Enter emoji code or alias: ").strip()

    # Convert the input to its emoji representation
    emojized_text = emoji.emojize(user_input, language='alias')

    # Output the result
    print(f"Output: {emojized_text}")

if __name__ == "__main__":
    main()
