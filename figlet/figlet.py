from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet_fonts = figlet.getFonts()


def main():
    if (len(sys.argv) == 1):
        handle_random_font()
    elif (len(sys.argv) == 3 and is_valid_sys_args()):
        handle_with_font()
    else:
        sys.exit("Invalid Usage")


def handle_random_font():
    user_input = input("Input: ")
    random_index = random.randint(0, len(figlet_fonts) - 1)

    figlet.setFont(font=figlet_fonts[random_index])
    print(figlet.renderText(user_input))


def handle_with_font():
    user_input = input("Input: ")
    user_font = sys.argv[2]

    figlet.setFont(font=user_font)
    print(figlet.renderText(user_input))


def is_valid_sys_args():
    return (((sys.argv[1] == "-f") or (sys.argv[1] == "--font")) and (sys.argv[2] in figlet_fonts))


if __name__ == "__main__":
    main()
