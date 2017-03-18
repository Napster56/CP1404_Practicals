"""
Program to convert a character to it's corresponding ASCII code and vice versa.
Program asks user if they wish to print the ASCII table
"""

import string

LOWER_NUM = 33
UPPER_NUM = 127


# Checks the number entered by user
def valid_num(user_number):
    while LOWER_NUM >= user_number <= UPPER_NUM:
        print("Please enter a number between 33 and 127.")
        user_number = int(input("Enter a number between 33 and 127: "))
    return user_number


# Print a table showing the characters for ASCII codes between 33 and 127
def print_table():
    print("Do you want to print the ASCII table from {} to {} ?".format(LOWER_NUM, UPPER_NUM))
    answer = input("Enter (Y) or (N)o: ")
    count = 0
    if answer.lower() == "y":
        print("How many columns do you want in the table?: ")
        columns = int(input("Enter the number of columns: "))
        rows = int((UPPER_NUM - LOWER_NUM + 1) / columns)
        print(rows)

        extra = 0
        if (rows * columns) != int(UPPER_NUM - LOWER_NUM + 1):
            extra += 1

        start = 0
        for column_number in range(1, columns + 1 + extra):
            end = rows * column_number
            list_of_ascii = range(LOWER_NUM, UPPER_NUM + 1)
            print(list_of_ascii[start:end])
            start = end

#        for i in range(LOWER_NUM, UPPER_NUM +1):
#            ascii_character = chr(i)
#            s = (i, ascii_character)
#            split = s.rsplit(" ", columns)
#            print(split)

    else:
        print("Goodbye")


def main():
    user_character = input("Enter a character: ")
    ascii_code = ord(user_character)
    print("The ASCII code for {} is {}".format(user_character, ascii_code))
    user_number = int(input("Enter a number between 33 and 127: "))
    user_number = valid_num(user_number)
    print(user_number)
    ascii_character = chr(user_number)
    print("The character for {} is {}".format(user_number, ascii_character))
    print_table()

main()
