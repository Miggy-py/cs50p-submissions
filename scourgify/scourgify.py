import sys
import csv
from typing import Tuple


def main():

    before_path, after_path = get_files()

    clean(before_path, after_path)


def get_files() -> Tuple[str, str]:
    ARGS_EXPECTED = 3

    if (len(sys.argv) < ARGS_EXPECTED):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > ARGS_EXPECTED):
        sys.exit("Too many command-line arguments")

    before_path = sys.argv[1].strip()
    after_path = sys.argv[2].strip()

    if (not(before_path.endswith(".csv")) or not(after_path.endswith(".csv"))):
        sys.exit("Not a CSV file")

    return (before_path, after_path)


def clean(before_path: str, after_path: str) -> None:
    new_fieldnames = ["first", "last", "house"]

    try:
        with open(before_path, "r") as before, open(after_path, "w") as after:
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames=new_fieldnames)
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(",")
                writer.writerow({new_fieldnames[0]: first.strip(),
                                 new_fieldnames[1]: last,
                                 new_fieldnames[2]: row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {before_path}")


if __name__ == "__main__":
    main()
