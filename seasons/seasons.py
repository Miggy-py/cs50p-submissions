from datetime import date
from datetime import timedelta
from typing import Tuple
import sys
import re
import inflect

"""
1. Get YYYY-MM-DD date from user, sys.exit if invalid (regex)
2. Find difference
3. Use timedelta.total_seconds()
4. Display using inflect: p.number_to_words

"""

p = inflect.engine()


def main():

    year, month, day = get_user_date()

    minutes = minutes_since(year, month, day)

    difference = minutes_to_words(minutes)

    print(f"{difference} minutes")


def get_user_date() -> tuple[int, int, int]:
    pattern = r"^(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})$"

    match = re.search(pattern, input("Date of Birth (YYYY-MM-DD): ").strip())

    if match is None:
        sys.exit("Invalid date")

    return (int(match.group("year")), int(match.group("month")), int(match.group("day")))


def minutes_since(year: int, month: int, day: int) -> int:
    today = date.today()
    users_date = date(year, month, day)

    return round((today - users_date).total_seconds() / 60)


def minutes_to_words(minutes: int) -> str:
    return (p.number_to_words(minutes, andword="")).capitalize()


if __name__ == "__main__":
    main()
