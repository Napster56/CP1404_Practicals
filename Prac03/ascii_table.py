"""
Program to convert a character to it's corresponding ASCII code and vice versa.

"""

LOWER_NUM = 33
UPPER_NUM = 127


# Gets number form user; checks for valid input and within given limits.
def get_number(LOWER_NUM, UPPER_NUM):
    valid_input = False
    while not valid_input:
        try:
            num = int(input("Enter a number between 10 and 100: "))
            valid_input = True
        except ValueError:
            print("Please enter a valid integer.")
        except:
            print("Ooops! Something went wrong!")
            print("The program will now close.")
    while num < LOWER_NUM or num > UPPER_NUM:
        print("Please enter a number between 33 and 127.")
        num = int(input("Enter a number between 33 and 127: "))
    return num


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
    user_number = get_number(LOWER_NUM, UPPER_NUM)
    print(user_number)
    ascii_character = chr(user_number)
    print("The character for {} is {}".format(user_number, ascii_character))
    print_table()

main()
