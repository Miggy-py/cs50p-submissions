import sys


def main():

    file_name = get_file()

    num_of_lines = get_line_count(file_name)

    print(num_of_lines)


def get_file() -> str:
    if (len(sys.argv) < 2):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1].strip()

    if (not file_name.endswith(".py")):
        sys.exit("Not a python file")

    return file_name


def get_line_count(file_name: str) -> int:
    # lines = []
    count = 0

    try:
        with open(f"{file_name}") as file:
            for line in file:
                stripped = line.strip()
                if ((not stripped.startswith("#")) and (len(stripped) > 0)):
                    count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    return count


if __name__ == "__main__":
    main()
