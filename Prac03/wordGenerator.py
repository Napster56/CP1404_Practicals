"""
CP1404/CP5632 - Practical 03
Random word generator - based on format of words using characters to represent vowels and/or consonants
"""

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def is_valid_format():
    for letter in word_format:
        if letter in "cv":
            return True
        else:
            return False

first_character = input("Select the character 'c' for consonants: ")
second_character = input("Select the character 'v' for vowels: ")
word_format = input("Enter your word format using {} for consonants and {} for vowels; if you enter an alphabetical \
\ncharacter, it will represent itself: ".format(first_character, second_character))
if word_format.lower() is False:
    print("Word format must use only the letters 'c' and/or 'v'. Enter a new format. ")
word_format = is_valid_format()
word = ""
for kind in word_format:
    if kind == first_character:
        word += random.choice(CONSONANTS)
    elif kind == second_character:
        word += random.choice(VOWELS)
    else:
        word += kind

print(word)