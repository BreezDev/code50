def main():
    output = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

    if output == "42":
        print("Yes")
    elif output == "forty-two":
        print("Yes")
    elif output == "forty two":
        print("Yes")
    elif output == "FoRty TwO":
        print("Yes")
    else:
        print("No")

main()
