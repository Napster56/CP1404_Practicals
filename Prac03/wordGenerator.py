"""
CP1404/CP5632 - Practical 03
Random word generator - based on format of words using characters to represent vowels and/or consonants
"""

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def is_valid_format(word_format):
    for letter in word_format:
        if "cv" in word_format:
            return True
        else:
            print(word_format)
            return False


def main():
    word_format = input("Enter your word format using 'C' for consonants and/or 'V' for vowels.")
    word_format = word_format.lower()
    result = is_valid_format(word_format)
    while result is False:
        print("Invalid word format.")
        word_format = input("Enter your word format using ONLY 'C' for consonants and/or 'V' for vowels.")
        result = is_valid_format(word_format)
        print(result)
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        elif kind == "v":
            word += random.choice(VOWELS)
    print(word)

main()

