def main():
    user_time = input("What time is it? ").strip()

    converted_time = convert(user_time)

    meridien_side = user_time.rsplit(" ", maxsplit=1)
    meal = get_meal(converted_time, meridien_side)

    print(meal)


def convert(time):
    hour, minute = time.split(":", maxsplit=1)

    hour = float(hour)
    minute = float(minute.split(" ", maxsplit=1)[0]) / 60

    return hour + minute


def get_meal(time, meridien_side):

    # print(time)
    # print(meridien_side)

    meridien_side = meridien_side[1] if len(meridien_side) == 2 else meridien_side[0]

    BREAKFAST_START, BREAKFAST_END = 7, 8
    LUNCH_START, LUNCH_END = 12, 13
    DINNER_START, DINNER_END = 18, 19

    if(meridien_side != 'a.m.' and meridien_side != 'p.m.'):
        if(time >= BREAKFAST_START and time <= BREAKFAST_END):
            return "breakfast time"
        elif(time >= LUNCH_START and time <= LUNCH_END):
            return "lunch time"
        elif(time >= DINNER_START and time <= DINNER_END):
            return "dinner time"
    else:
        if(meridien_side == 'a.m.' and time >= BREAKFAST_START and time <= BREAKFAST_END):
            return "breakfast time"
        elif(meridien_side == 'p.m.'):
            if(time >= LUNCH_START and (time <= LUNCH_END or (time + 12 <= LUNCH_END))):
                return "lunch time"
            elif((time >= DINNER_START or (time + 12 >= DINNER_START)) and (time <= DINNER_END or (time + 12 <= DINNER_END))):
                return "dinner time"

    return ""


if __name__ == "__main__":
    main()
