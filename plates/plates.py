def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if ((not s[0:2].isalpha()) or (len(s) < 2) or (len(s) > 6) or (not s[-1].isalnum())):
        return False

    for i in range(2, len(s) - 1):
        if(not s[i].isalnum()):
            return False

        if((s[i].isdigit() and not s[i + 1].isdigit())):
            return False

        if(s[i] == "0" and not s[i - 1].isdigit()):
            return False

    return True


if __name__ == "__main__":
    main()
