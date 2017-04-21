"""
Program asks user for the date-of-birth details for 5 people, and displays their individual ages by using a dictionary.
"""

import datetime


# def add_date(name, birth_date, birth_date_dict):
#    birth_date_dict[name] = birth_date


def calc_age(birth_date):
    day, month, year = birth_date.split("/")
    birth_day = int(day)
    birth_month = int(month)
    birth_year = int(year)
    now = datetime.date.today()
    this_year = now.year
    age = this_year - birth_year
    if now.month < birth_month or now.month == birth_month and now.day < birth_day:
        age = this_year - birth_year - 1
    return age


def print_ages(birth_date_dict):
    for name, age in birth_date_dict.items():
        print("{} is {} years old".format(name, age))


def main():
    birth_date_dict = {}
    for i in range(5):
        name = input("Enter the person's name: ")
        birth_date = input("Enter the person's date of birth: ")
        birth_date_dict[name] = birth_date
        age = calc_age(birth_date)
        birth_date_dict[name] = age
    print_ages(birth_date_dict)
main()
