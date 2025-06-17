import sys
import csv
from tabulate import tabulate
from typing import List


def main():

    file_name = get_file()

    menu = get_menu_from(file_name)

    display_tabulated_menu(menu)


def get_file() -> str:
    if (len(sys.argv) < 2):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1].strip()

    if (not file_name.endswith(".csv")):
        sys.exit("Not a CSV file")

    return file_name


def get_menu_from(file_name: str) -> List[List[str]]:
    menu = []

    try:
        with open(f"{file_name}") as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    return menu


def display_tabulated_menu(menu: List[List[str]]) -> None:
    print(tabulate(menu, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
