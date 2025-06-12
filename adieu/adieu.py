import inflect

p = inflect.engine()


def main():
    name_list = get_names()

    say_adieu_to(name_list)


def get_names():
    name_list = []

    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            break

    return name_list


def say_adieu_to(name_list):
    print(f"Adieu, adieu, to {p.join(name_list)}")


if __name__ == "__main__":
    main()
