def main():
    camel_case = input("camelCase: ").strip()
    snake_case = camel_to_snake(camel_case)
    print(f"snake_case: {snake_case}")

def camel_to_snake(camel):
    snake = ""
    for char in camel:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

if __name__ == "__main__":
    main()
