"""
CP1404/CP5632 - Practical
Random password generator based on the following:
    -

(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""
import random

import string

password_length = int(input("Enter the length of the password: "))
uppercase = input("Are uppercase letters required for the password: ")
lowercase = input("Are lowercase letters required for the password: ")
digits = input("Are numerals required for the password: ")
special = input("Are special characters required for the password: ")
password = " "
if uppercase == "y" and lowercase == "y" and special == "y" and digits == "y":
    for i in range(password_length):
        characters = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
        password += random.choice(characters)
elif uppercase == "y" and lowercase == "y" and special == "y" and digits == "n":
    for i in range(password_length):
        characters = (string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
        password += random.choice(characters)
elif uppercase == "y" and lowercase == "y" and special == "n" and digits == "n":
    for i in range(password_length):
        characters = (string.ascii_lowercase + string.ascii_uppercase)
        password += random.choice(characters)
elif uppercase == "y" and lowercase == "n" and special == "n" and digits == "n":
    for i in range(password_length):
        characters = string.ascii_uppercase
        password += random.choice(characters)
elif uppercase == "y" and lowercase == "n" and special == "y" and digits == "n":
    for i in range(password_length):
        characters = (string.ascii_uppercase + string.punctuation)
        password += random.choice(characters)
elif uppercase == "n" and lowercase == "y" and special == "y" and digits == "y":
    for i in range(password_length):
        characters = (string.ascii_lowercase + string.punctuation + string.digits)
        password += random.choice(characters)
elif uppercase == "n" and lowercase == "n" and special == "y" and digits == "n":
    for i in range(password_length):
        characters = string.punctuation
        password += random.choice(characters)
elif uppercase == "y" and lowercase == "n" and special == "y" and digits == "n":
    for i in range(password_length):
        characters = (string.ascii_uppercase + string.punctuation)
        password += random.choice(characters)

print(password)
