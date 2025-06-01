def main():
    mass = int(input("m: "))

    E = einsteins(mass)

    print(f"E: {E}")


def einsteins(m):
    return m * (300000000 ** 2)


if __name__ == "__main__":
    main()
