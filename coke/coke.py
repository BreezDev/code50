def main():
    total = 0
    cost = 50
    print("Insert coins (25, 10, 5 cents).")

    while total < cost:
        coin = int(input("Insert coin: "))
        if coin in [25, 10, 5]:
            total += coin
            if total < cost:
                print(f"Amount Due: {cost - total}")
        else:
            print(f"Amount Due: {cost - total}")

    print(f"Change Owed: {total - cost}")

if __name__ == "__main__":
    main()
