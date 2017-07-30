"""
Write a program to get the number of rows from the user and calculate the number of blocks
you will need given the number of rows (n) to make a 2D pyramid.

"""

rows = int(input("Enter the number of rows in the pyramid: "))


# using a for loop
def calculate_blocks(n):
    blocks = 0
    while n > 0:
        blocks += n
        n -= 1
    print(blocks)


calculate_blocks(rows)


# recursively
def calc_blocks_recursively(n):
    if n == 1:
        return 1
    return n + calc_blocks_recursively(n - 1)


print(calc_blocks_recursively(rows))
