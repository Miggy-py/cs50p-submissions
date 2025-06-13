def main():
    user_word = input("Input: ")

    print(f"Output: {shorten(user_word)}")



def shorten(word: str) -> str:
    VOWELS = {"a", "e", "i", "o", "u"}
    shortened_word_list = []

    for char in word:
        if (char.lower() not in VOWELS):
            shortened_word_list.append(char)

    return "".join(shortened_word_list)


if __name__ == "__main__":
    main()
