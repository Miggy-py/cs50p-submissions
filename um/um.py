import re


def main():
    print(count(input("Text: ")))


def count(s: str) -> int:
    pattern = r"\b[^a-z]*(um)[^a-z]*\b"

    matches = re.findall(pattern, s, flags=re.IGNORECASE)

    return len(matches)


if __name__ == "__main__":
    main()
