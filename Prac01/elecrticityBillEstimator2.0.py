"""
Program to estimate the cost of electricity by:
- asking the user to choose between two tariffs
- the daily use in kWh, and
- the number of days in the billing period.
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def get_tariff():
    choice = int(input("Enter the tariff being used."))
    while choice != 11 and choice != 31:
        print("Invalid input.")
        choice = int(input("Enter the tariff being used."))
    if choice == 11:
        tariff = TARIFF_11
        return tariff
    elif choice == 31:
        tariff = TARIFF_31
        return tariff

def get_num(prompt):
    num = float(input(prompt))
    while num < 0:
        print("Invalid input.")
        num = int(input(prompt))
    return num


def main():
    tariff = get_tariff()
    daily_use_kwh = get_num("Enter daily use in kWh: ")
    billing_days = get_num("Enter number of billing days: ")
    estimated_cost = tariff * daily_use_kwh * billing_days
    print("Estimated bill is: $ {:.2f} ".format(estimated_cost))

main()