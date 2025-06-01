def main():
    inputtedMsg = input()

    print(convertFaces(inputtedMsg))


def convertFaces(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == "__main__":
    main()
