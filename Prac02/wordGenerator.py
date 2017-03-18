"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


first_character = input("Select a character for consonants: ")
second_character = input("Select a character for vowels: ")
word_format = input("Enter your word format using {} for consonants and {} for vowels; if you enter an alphabetical \
\ncharacter, it will represent itself: ".format(first_character, second_character))
word_format.lower()
word = ""
for kind in word_format:
    if kind == first_character:
        word += random.choice(CONSONANTS)
    elif kind == second_character:
        word += random.choice(VOWELS)
    else:
        word += kind

print(word)