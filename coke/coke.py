def main():
    amount_due = 50

    while True:

        print(f"Amount due: {amount_due}")

        coin = int(input("Insert coin: "))

        amount_due = handle_coin_input(amount_due, coin)

        if (amount_due <= 0):
            break

    change = handle_change(amount_due)

    print(f"Change Owed: {change}")


def handle_change(amount_due):
    return amount_due * -1


def handle_coin_input(amount_due, coin):
    accepted_coins = [5, 10, 25]

    if (coin in accepted_coins):
        amount_due -= coin

    return amount_due


if __name__ == "__main__":
    main()
