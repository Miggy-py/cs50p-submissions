def main():

    fuel = get_fuel_input()

    fuel_level = interpret_fuel(fuel)

    display_fuel(fuel_level)


def get_fuel_input():
    MAX_FUEL = 1
    MIN_FUEL = 0

    FIRST_ELEMENT = 0
    SECOND_ELEMENT = 1

    while True:
        fuel_input = input("Fraction: ").strip()
        elements = fuel_input.split("/")

        try:
            fuel_float = int(elements[FIRST_ELEMENT]) / int(elements[SECOND_ELEMENT])

            if(fuel_float > MAX_FUEL or fuel_float < MIN_FUEL):
                raise ValueError

            return str(round(fuel_float * 100))

        except (ValueError, ZeroDivisionError):
            pass


def interpret_fuel(fuel):
    TANK_FULL = 99
    TANK_EMPTY = 1

    if (int(fuel) >= TANK_FULL):
        return "F"
    elif (int(fuel) <= TANK_EMPTY):
        return "E"
    return fuel


def display_fuel(fuel_level):
    print(f"{fuel_level}") if fuel_level.isalpha() else print(f"{fuel_level}%")


if __name__ == "__main__":
    main()
