"""CP1404 Practical07 - Client code to use the Guitar class."""

from Prac07.guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.4)
    guitar2 = Guitar("Fender Eric Clapton Stratocaster®", 1991, 3599)


    print(guitar1)
    #guitar1.get_age(age)

    print("get_age() - Expected 95. Got {}".format(guitar1.get_age()))
    print("get_age() - Expected 26. Got {}".format(guitar2.get_age()))

    age1 = guitar1.get_age()
    age2 = guitar2.get_age()

    print("is_vintage() - Expected True. Got {}".format(guitar1.is_vintage(age1)))
    print("get_age() - Expected False. Got {}".format(guitar2.is_vintage(age2)))

main()
