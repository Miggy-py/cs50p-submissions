import random


def main():
    level_chosen = get_level_from_user()

    start_game_with(level_chosen)


def get_level_from_user():
    while True:
        try:
            level_chosen = int(input("Level: "))
            if (level_chosen < 1): raise ValueError
            break
        except ValueError:
            pass

    return level_chosen


def start_game_with(level_chosen):
    random_number = random.randint(1, level_chosen)

    while True:
        try:
            user_guess = int(input("Guess: "))
        except ValueError:
            continue

        if (user_guess == random_number):
            print("Just right!")
            break
        elif (user_guess < random_number):
            print("Too small!")
        else:
            print("Too large!")


if __name__ == "__main__":
    main()
