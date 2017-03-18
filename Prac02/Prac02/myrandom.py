

import random

import string

UPPER = string.uppercase

LOWER = string.lowercase

SPECIAL = string.punctuation

password = []
password_length = int(input("Enter the  length of the password: "))

for i in range(password_length):
    random_upper = random.choice(UPPER)
    password.append(random_upper)
print(password)
