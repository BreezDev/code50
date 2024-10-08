def main():
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "blueberries": 80,
        "cantaloupe": 60,
        "cherry": 50,
        "grape": 90,
        "grapefruit": 80,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "mango": 150,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 80,
        "plum": 70,
        "raspberry": 60,
        "strawberry": 50,
        "sweet cherries": 100
    }

    fruit = input("Fruit: ").strip().lower()
    if fruit in fruit_calories:
        print(f"Calories: {fruit_calories[fruit]}")

if __name__ == "__main__":
    main()
