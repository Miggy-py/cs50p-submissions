import requests
import sys
import json

COINCAP_KEY = ""


def main():
    user_coin = handle_command_line_arg()
    bitcoin_price = get_bitcoin_price()

    amount = user_coin * bitcoin_price

    print(f"${amount:,.4f}")


def handle_command_line_arg():
    if (len(sys.argv) < 2):
        sys.exit("Missing command-line argument")
    try:
        float_input = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    return float_input

def get_bitcoin_price():
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + COINCAP_KEY
        )
    except requests.RequestException:
        sys.exit("Bad request to API")

    o = response.json()

    price = float(o.get("data").get("priceUsd"))

    return price


if __name__ == "__main__":
    main()
