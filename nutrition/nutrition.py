def main():

    user_fruit = input("Item: ").lower()

    calories = calories_from_fruit(user_fruit)

    if calories != None:
        print(f"Calories: {calories}")


def calories_from_fruit(user_fruit):
    FRUITS = {
        "apple":"130",
        "avocado":"50",
        "banana":"110",
        "cantaloupe":"50",
        "grapefruit":"60",
        "grapes":"90",
        "honeydew melon":"50",
        "kiwifruit":"90",
        "lemon":"15",
        "lime":"20",
        "nectarine":"60",
        "orange":"80",
        "peach":"60",
        "pear":"100",
        "pineapple":"50",
        "plums":"70",
        "strawberries":"50",
        "sweet cherries":"100",
        "tangerine":"50",
        "watermelon":"80"
    }

    return FRUITS.get(user_fruit)


if __name__ == "__main__":
    main()
