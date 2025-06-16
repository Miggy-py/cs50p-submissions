def main():

    user_input = input("Greeting: ")

    money = value(user_input)

    print(f"${money}")


def value(user_input):
    user_input = user_input.strip().lower()

    if (user_input.startswith("hello")):
        return 0
    elif (user_input.startswith("h")):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
