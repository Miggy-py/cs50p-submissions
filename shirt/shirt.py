import sys
from PIL import Image, ImageOps
from typing import Tuple


def main():

    before_path, after_path = get_files()

    apply_cs50_shirt(before_path, after_path)


def get_files() -> Tuple[str, str]:
    ARGS_EXPECTED = 3

    if (len(sys.argv) < ARGS_EXPECTED):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > ARGS_EXPECTED):
        sys.exit("Too many command-line arguments")

    before_path = sys.argv[1].strip()
    after_path = sys.argv[2].strip()

    if (not file_extensions_equals(before_path, after_path)):
        sys.exit("Input and output have different extensions")

    return (before_path, after_path)


def file_extensions_equals(before_path: str, after_path: str) -> bool:
    supported_extensions = {"jpg", "jpeg", "png"}

    before_partitioned = before_path.rpartition(".")
    after_partitioned = after_path.rpartition(".")

    before_extension = before_partitioned[2].lower()
    after_extension = after_partitioned[2].lower()

    if ((before_extension not in supported_extensions) or
        (after_extension not in supported_extensions)):
        sys.exit("Invalid input")

    return before_extension == after_extension


def apply_cs50_shirt(before_path: str, after_path: str) -> None:
    try:
        with Image.open(before_path) as img:
            shirt = Image.open("shirt.png")
            size = shirt.size

            img = ImageOps.fit(img, size)
            img.paste(shirt, shirt)

            img.save(after_path)
            shirt.close()

    except FileNotFoundError:
        sys.exit(f"Could not read files")


if __name__ == "__main__":
    main()
