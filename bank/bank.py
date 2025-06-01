def main():

    user_input = input("Greeting: ").strip().lower()

    money = get_greeting_money(user_input)

    print(f"${money}")


def get_greeting_money(user_input):

    if (user_input.startswith("hello")):
        return 0
    elif (user_input.startswith("h")):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
