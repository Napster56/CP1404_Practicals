"""
Program to calculate total shipping charge
for a number of items, each with different prices.
If the total shipping cost is over $100, then a 10%
discount is applied to the total shipping cost before
the amount is displayed on the screen.
"""


def get_shipping_charge():
    shipping_cost = float(input('Enter the shipping cost of the item.'))
    return shipping_cost


def main():
    num_items = int(input('Enter the number of items to be shipped.'))
    while num_items < 0:
        print('Invalid number of items.')
        num_items = int(input('Enter the number of items to be shipped.'))
    total_shipping_cost = 0
    for i in range(num_items):
        total_shipping_cost += get_shipping_charge()
    if total_shipping_cost > 100:
        total_shipping_cost = total_shipping_cost * 0.9
    print("The total shipping cost is: $", total_shipping_cost)

main()
