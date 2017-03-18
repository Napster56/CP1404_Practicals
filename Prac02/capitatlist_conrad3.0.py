import random

max_increase = random.randint(0, 25)
max_decrease = random.randint(0, 35)
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 100.0
count = 0

price = INITIAL_PRICE
print("Starting price is: ${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, max_increase)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        price_change = random.uniform(-max_decrease, 0)

    price *= (1 + price_change)
    count += 1

    if count > 0:
        print("On day", count, "price is: ${:,.2f}".format(price))
