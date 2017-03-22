"""
CP1404/CP5632 - Practical 03
Random word generator - based on format of words using characters to represent vowels and/or consonants
"""

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def is_valid_format(word_format):
    for letter in word_format:
        if letter in "cv":
            return True
        else:
            return False


def main():
    word_format = input("Enter your word format using 'C' for consonants and/or 'V' for vowels.")
    if is_valid_format(word_format) is True:
        word = ""
        for kind in valid_format:
            if kind == "c":
                word += random.choice(CONSONANTS)
            elif kind == "v":
                word += random.choice(VOWELS)
            else:
                word += kind
        print(word)
    else:
        print("Invalid word format. Enter a new format. ")
        word_format = input("Enter your word format using 'C' for consonants and/or 'V' for vowels.")
main()