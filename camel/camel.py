def main():

    user_input = input("camelCase: ").strip()

    print_as_snake_case(user_input)


def print_as_snake_case(user_str):
    print("snake_case: ", end="")
    for char in user_str:
        if(char.isupper()):
            print("_" + char.lower(), end="")
        else:
            print(char, end="")

    print("")


if __name__ == "__main__":
    main()
