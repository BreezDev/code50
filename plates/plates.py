def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[0:2].isalpha():
        return False
    for char in s:
        if not (char.isalpha() or char.isdigit()):
            return False

    has_numbers = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not has_numbers and char == '0':
                return False
            has_numbers = True
        elif has_numbers:
            return False

    return True

if __name__ == "__main__":
    main()
