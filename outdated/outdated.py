months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}


YEAR_INDEX = 2
DAY_INDEX = 1
MONTH_INDEX = 0


def main():
    handle_date_values()


def handle_date_values():

    while True:
        user_input = input("Date: ").strip()
        split_values = ""

        if "/" in user_input:
            split_values = user_input.split("/")
            date_tuple = clean_numeric_date(split_values)
        elif " " in user_input:
            split_values = user_input.split(" ")
            date_tuple = clean_strmonth_date(split_values)
        else:
            continue

        if (date_tuple is None): continue

        print(f"{date_tuple[0]}-{date_tuple[1]:02}-{date_tuple[2]:02}")
        break


def clean_strmonth_date(split_values):

    if len(split_values) > 3: return None

    try:

        year = int(split_values[YEAR_INDEX])
        if "," not in split_values[DAY_INDEX]: raise ValueError
        str_day = "".join([char for char in split_values[DAY_INDEX] if char.isdigit()])
        day = int(str_day)
        month = months[split_values[MONTH_INDEX]]

        if not (day > 0 and day < 32):
            raise ValueError

    except (KeyError, IndexError, ValueError):
        return None

    date_tuple = year, month, day

    return date_tuple


def clean_numeric_date(split_values):

    if len(split_values) > 3: return None

    try:

        year = int(split_values[YEAR_INDEX])
        day = int(split_values[DAY_INDEX])
        month = int(split_values[MONTH_INDEX])

        if not valid_date_ints(day, month):
            raise ValueError

    except (IndexError, ValueError):
        return None

    date_tuple = year, month, day

    return date_tuple


def valid_date_ints(day, month):
    return ( (day > 0) and (day < 32) and (month > 0) and (month < 13))


if __name__ == "__main__":
    main()
