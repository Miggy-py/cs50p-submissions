menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    handle_user_order()


def handle_user_order():
    total = 0

    while True:
        try:
            entree = input("Item: ").strip().title()
        except EOFError:
            print("")
            break

        try:
            total += menu[entree]
            print(f"Total: ${total:.2f}")
        except KeyError:
            pass


if __name__ == "__main__":
    main()
