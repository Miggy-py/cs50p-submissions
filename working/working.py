import re


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    s = s.strip().lower()

    pattern = r"^(?P<initial_hour>[0-9][0-9]?):?(?P<initial_minute>[0-9]{2})?\s+(?P<initial_merid>am|pm)\s+to\s+(?P<end_hour>[0-9][0-9]?):?(?P<end_minute>[0-9]{2})?\s+(?P<end_merid>am|pm)$"

    match = re.search(pattern, s, flags=re.IGNORECASE)

    if match is None:
        raise ValueError

    initial_hour = int(match.group("initial_hour"))
    initial_minute = int(match.group("initial_minute")) if match.group("initial_minute") is not None else 0
    end_hour = int(match.group("end_hour"))
    end_minute = int(match.group("end_minute")) if match.group("end_minute") is not None else 0

    if not is_valid_time(initial_hour, initial_minute, end_hour, end_minute):
        raise ValueError

    initial_merid = match.group("initial_merid")
    end_merid = match.group("end_merid")

    initial_hour, end_hour = adjust_hours(initial_merid, initial_hour, end_merid, end_hour)

    return f"{initial_hour:02}:{initial_minute:02} to {end_hour:02}:{end_minute:02}"


def adjust_hours(initial_merid, initial_hour, end_merid, end_hour):
    if (initial_merid == "pm"):
        initial_hour += 12
    elif (initial_merid == "am" and initial_hour == 12):
        initial_hour = 0

    if (end_merid == "pm" and end_hour != 12):
        end_hour += 12

    return initial_hour, end_hour


def is_valid_time(initial_hour: int, initial_minute: int, end_hour: int, end_minute: int) -> bool:
    return initial_hour <= 12 and end_hour <= 12 and initial_minute <= 59 and end_minute <= 59


if __name__ == "__main__":
    main()
