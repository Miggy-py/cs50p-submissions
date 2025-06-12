import emoji


def main():

    user_input = input("Input: ")

    print(f"Output: {emojize_string(user_input)}")


def emojize_string(user_input):
    return emoji.emojize(user_input, language='alias')


if __name__ == "__main__":
    main()
