import validators


def main():
    email = input("What's your email address? ")

    print("Valid") if validate(email) else print("Invalid")


def validate(email):
    return validators.email(email)


if __name__ == "__main__":
    main()
