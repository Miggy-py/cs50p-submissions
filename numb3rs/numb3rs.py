import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"

    match = re.search(pattern, ip.strip())

    if match is None:
        return False

    numbers = [int(num) for num in match.groups()]
    for number in numbers:
        if number > 255:
            return False

    return True


if __name__ == "__main__":
    main()
