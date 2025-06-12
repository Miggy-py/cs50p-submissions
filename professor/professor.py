import random


def main():
    level = get_level()

    start_game(level)


def get_level():
    accepted_levels = [1,2,3]

    while True:
        try:
            user_level = int(input("Level: "))
            if (user_level not in accepted_levels): raise ValueError
            break
        except ValueError:
            pass

    return user_level


def start_game(level):
    MAX_TRIES = 3
    NUMBER_OF_PROBLEMS = 10
    score = NUMBER_OF_PROBLEMS

    for i in range(0, NUMBER_OF_PROBLEMS):
        first_int = generate_integer(level)
        second_int = generate_integer(level)
        correct_answer = first_int + second_int

        for i in range(MAX_TRIES):
            try:
                user_input = int(input(f"{first_int} + {second_int} = "))
                if (user_input == correct_answer):
                    break
            except ValueError:
                pass

            if (i == MAX_TRIES - 1):
                print(f"{first_int} + {second_int} = {correct_answer}")
                score -= 1
                break

            print("EEE")

    print(f"Score: {score}")


def generate_integer(level):
    if (level == 1):
        return random.randint(0, 9)
    elif (level == 2):
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
