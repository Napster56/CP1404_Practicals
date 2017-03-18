"""
CP1404/CP5632 - Practical
Program generates a random password:
    - gets length of password from the user
    - uses lowercase characters and numerals for all passwords as a minimum
    - then asks user if uppercase and/or special characters are required
"""

import random

import string

print("The password must contain lowercase characters and number; however, you may specify if you want to include \
special characters and/or uppercase characters.")
password_length = int(input("Enter the length of the password: "))
uppercase = input("Are uppercase letters required for the password: ")
special = input("Are special characters required for the password: ")
password = " "
if uppercase == "y" and special == "y":
    for i in range(password_length):
        characters = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
        password += random.choice(characters)
elif uppercase == "n" and special == "y":
    for i in range(password_length):
        characters = (string.ascii_lowercase + string.digits + string.punctuation)
        password += random.choice(characters)
elif uppercase == "y" and special == "n":
    for i in range(password_length):
        characters = (string.ascii_lowercase + string.ascii_uppercase + string.digits)
        password += random.choice(characters)
elif uppercase == "n" and special == "n":
    for i in range(password_length):
        characters = (string.ascii_lowercase + string.digits)
        password += random.choice(characters)
print(password)
