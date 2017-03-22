"""
Program to convert a character to it's corresponding ASCII code and vice versa.
"""

LOWER_NUM = 33
UPPER_NUM = 127


# Checks the number entered by user
def valid_num(user_number):
    while user_number < LOWER_NUM  or user_number > UPPER_NUM:
        print("Please enter a number between 33 and 127.")
        user_number = int(input("Enter a number between 33 and 127: "))
    return user_number


# Print a table showing the characters for ASCII codes between 33 and 127
def print_table():
    print("Do you want to print the ASCII table from {} to {} ?".format(LOWER_NUM, UPPER_NUM))
    answer = input("Enter (Y) or (N)o: ")
    if answer.lower() == "y":
        print("How many columns do you want in the table?: ")
        for i in range(LOWER_NUM, UPPER_NUM + 1):
            ascii_character = chr(i)
            print("{:>5}{:>10s}".format(i, ascii_character))
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
