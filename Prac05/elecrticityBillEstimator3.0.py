"""
Program to estimate the cost of electricity by:
- asking the user to choose tariffs stored in a dictionary
- the daily use in kWh, and
- the number of days in the billing period.
"""


def get_tariff(tariff_dict):
    print("Select from the following tariffs: ")
    for key in tariff_dict:
        print("{:>5}".format(key))
    choice = input("Enter the tariff being used.")
    while choice not in tariff_dict.keys():
        print("Invalid input.")
        choice = input("Enter the tariff being used.")
    tariff = tariff_dict[choice]
    return tariff

'''
def add_to_dictionary(tariff_dict):
    new_tariff = input("Do you wish to add a new tariff: ")
    if new_tariff == "yes".upper():
        tariff = get_num("Enter the tariff code: ")
        rate = get_num("Enter the tariff rate: ")
        tariff_dict[tariff] = rate
'''


def get_num(prompt):
    num = float(input(prompt))
    while num < 0:
        print("Invalid input.")
        num = int(input(prompt))
    return num


def main():
    tariff_dict = {'11': 0.244618, '31': 0.136928}
    tariff = get_tariff(tariff_dict)
    # add_to_dictionary(tariff_dict)
    daily_use_kwh = get_num("Enter daily use in kWh: ")
    billing_days = get_num("Enter number of billing days: ")
    estimated_cost = tariff * daily_use_kwh * billing_days
    print("Estimated bill is: ${:.2f} ".format(estimated_cost))

main()