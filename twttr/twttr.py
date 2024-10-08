def main():
    text = input("Enter text: ")
    vowels = "aeiouAEIOU"
    result = ''.join(c for c in text if c not in vowels)
    print(result)

if __name__ == "__main__":
    main()
