"""
Program asks user for the date-of-birth details for 5 people, and displays their individual ages by using a dictionary.
"""

#TODO Finish this!!!!

birth_date_dict = {}


def add_date(name, birth_date):
    birth_date_dict[name] = birth_date
    print(birth_date_dict)


def main():
    name = input("Enter the person's name: ")
    birth_date = input("Enter the person's date of birth: ")
    for i in range(5):
        add_date(name, birth_date)
        name = input("Enter the person's name: ")
        birth_date = input("Enter the person's date of birth: ")
        i += 1

main()