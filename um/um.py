import re


def main():
    print(count(input("Text: ")))


def count(s: str) -> int:
    s = s.strip()

    pattern = r"\b[^a-z]*(um)[^a-z]*\b"

    matches = re.findall(pattern, s, flags=re.IGNORECASE)

    print(matches)

    if matches is None:
        return 0

    return len(matches)


if __name__ == "__main__":
    main()
