"""
Program asks user for the date-of-birth details for 5 people, and displays their individual ages by using a dictionary.
"""

import datetime



def add_date(name, birth_date, birth_date_dict):
    birth_date_dict[name] = birth_date


def calc_age(birth_date):
    day, month, year = birth_date.split("/")
    birth_year = int(year)
    this_year = datetime.datetime.now().year
    age = this_year - birth_year
    return age


def print_ages(all_ages, age):
    for name in all_ages:
        print("{} is {} years old".format(name, age))


def main():
    birth_date_dict = {}
    all_ages = []
    for i in range(2):
        name = input("Enter the person's name: ")
        birth_date = input("Enter the person's date of birth: ")
        add_date(name, birth_date, birth_date_dict)
        age = calc_age(birth_date)
        print_ages(age, name)


main()
