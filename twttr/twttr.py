def main():
    user_input = input("Input: ")

    print("Output: ", end ="")
    print_without_vowels(user_input)


def print_without_vowels(user_input):
    VOWELS = ["a", "e", "i", "o", "u"]

    for char in user_input:
        if (char.lower() not in VOWELS):
            print(f"{char}", end="")

    print("")


if __name__ == "__main__":
    main()
