"""
Program to ask user
"""

rows = int(input("How many rows?:"))

# calculate pyramid blocks using while loop
# sum = 0
# while rows > 0:
#     sum += rows
#     rows -= 1
# print(sum)

# calculate pyramid blocks using recursion

def pyramid_blocks_rec(rows, total = 0):
    if rows == 0:
        print(total)
        return
    total += rows
    pyramid_blocks_rec(rows - 1, total)

pyramid_blocks_rec(rows)