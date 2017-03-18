"""
Program to estimate the cost of electricity using:
- the price per kWh in cents,
- the daily use in kWh, and
- the number of days in the billing period.
"""


def get_num(prompt):
    num = float(input(prompt))
    while num < 0:
        print("Invalid input.")
        num = int(input(prompt))
    return num


def main():
    cost_per_kwh = get_num("Enter the price per kWh in cents: ")
    daily_use_kwh = get_num("Enter daily use in kWh: ")
    billing_days = get_num("Enter number of billing days: ")
    estimated_cost = cost_per_kwh / 100 * daily_use_kwh * billing_days
    print("Estimated bill is: $ {:.2f} ".format(estimated_cost))

main()