"""
Program to convert a character to it's corresponding ASCII code and vice versa.
"""

#Gets lower and upper limits from user
def get_number(lower, upper):
    num = int(input("Enter a number between 10 and 100: "))
    try:
        (lower, upper) = int(input("Enter a number between 10 and 100: "))
    except ValueError:
        print("Please enter a valid integer.")
    except num < 0:
        print("Please enter a positive integer.")
    except:
        print("Ooops! Something went wrong!")
    print("The program will now close.")


# Checks number is within limits
def check_number(lower, upper)
    while lower > user_number < upper:
        print("Please enter a number between {} and {}.".format(lower, upper))
        user_number = int(input("Enter a number between {} and {}.".format(lower, upper))
    return user_number


def main():
    lower = get_num("Enter the lower limit (10 - 49): ")
    upper = get_num("Enter the upper limit (50 - 100): ")
    valid_num = get_number(lower, upper):
    user_character = input("Enter a character: ")
    ascii_code = ord(user_character)
    print("The ASCII code for {} is {}".format(user_character, ascii_code))
    user_number = get_number()
        valid_num(user_number)
    print(user_number)
    ascii_character = chr(user_number)
    print("The character for {} is {}".format(user_number, ascii_character))
    print_table()

main()
