import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str:
    embed_pattern = r"^<iframe.*src=\"(https?://(?:www\.)?youtube\.com/embed/[a-z0-9]+)\".*></iframe>$"

    match = re.search(embed_pattern, s.strip(), flags=re.IGNORECASE)

    if match is None:
        return None

    embed_link = match.group(1)

    parse_pattern = r"https?://(?:www\.)?youtube\.com/embed/"

    parsed_link = re.sub(parse_pattern, "https://youtu.be/", embed_link)

    return parsed_link


if __name__ == "__main__":
    main()
