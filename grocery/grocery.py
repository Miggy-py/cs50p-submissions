grocery = {}


def main():
    handle_grocery_inputs()


def handle_grocery_inputs():

    while True:
        try:
            item = input("").strip().upper()
        except EOFError:
            print("")
            print_grocery_sorted()
            break

        grocery[item] = grocery.get(item, 0) + 1


def print_grocery_sorted():
    for item in sorted(grocery):
        print(f"{grocery[item]} {item}")


if __name__ == "__main__":
    main()
