def main():

    fuel = get_fuel_input()

    fuel_level = gauge(fuel)

    print(fuel_level)


def get_fuel_input():
    while True:
        fuel_input = input("Fraction: ").strip()

        try:
            converted = convert(fuel_input)
        except (ValueError, ZeroDivisionError, IndexError):
            continue

        return converted


def convert(fraction):
    MAX_FUEL = 1
    MIN_FUEL = 0

    FIRST_ELEMENT = 0
    SECOND_ELEMENT = 1

    elements = fraction.split("/")

    try:
        first = int(elements[FIRST_ELEMENT])
        second = int(elements[SECOND_ELEMENT])

        if(second == 0):
            raise ZeroDivisionError

        fuel_float = first/second

        if(fuel_float > MAX_FUEL or fuel_float < MIN_FUEL):
            raise ValueError

        return (round(fuel_float * 100))

    except (ValueError, IndexError):
        raise ValueError


def gauge(fuel):
    TANK_FULL = 99
    TANK_EMPTY = 1

    if (int(fuel) >= TANK_FULL):
        return "F"
    elif (int(fuel) <= TANK_EMPTY):
        return "E"
    return f"{fuel}%"


if __name__ == "__main__":
    main()
