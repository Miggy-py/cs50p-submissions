def main():

    user_input = input("Expression: ").strip()

    first, operator, second = user_input.split(" ")

    output = calculate(float(first), operator, float(second))

    print(output)


def calculate(first, operator, second):
    if(operator == "+"):
        return first + second
    elif(operator == "-"):
        return first - second
    elif(operator == "*"):
        return first * second
    elif(operator == "/"):
        return first / second
    else:
        return "Invalid input"


if __name__ == "__main__":
    main()
