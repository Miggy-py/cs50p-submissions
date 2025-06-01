def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    # print(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # print(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return clean_float(d)


def percent_to_float(p):
    return clean_float(p)


def clean_float(uncleaned):
    filtered = ""
    for char in uncleaned:
        if(char.isdigit()):
            filtered += char

    filtered = float(filtered) / 100
    return filtered


if __name__ == "__main__":
    main()
