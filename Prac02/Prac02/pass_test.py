import random

import string


password_length = int(input("Enter the length of the password: "))
uppercase = input("Are uppercase letters required for the password: ")
lower = input("Are lowercase letters required for the password: ")
digits = input("Are numerals required for the password: ")
special = input("Are special characters required for the password: ")
password = " "
if uppercase == 'y': # or lower.lower == 'y' or special.lower == 'y' or digits.lower == "y":
    for i in range(password_length):
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password += random.choice(characters)
print(password)