def main():
    text = input("Enter text: ")
    result = shorten(text)
    print(result)

def shorten(word):
    vowels = "aeiouAEIOU"
    return ''.join(c for c in word if c not in vowels)



if __name__ == "__main__":
    main()
