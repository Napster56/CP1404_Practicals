import random
import string

def id_generator(chars=string.ascii_lowercase, size=1):
    return ''.join(random.choice(chars) for _ in range(size))

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxz"

def main():
    print("Word layout:\n'C' = random consonant\n'V' = random vowel\n'X' = random letter\n'{any lowercase letter}' = any constant letter\n")
    layout = input("Enter the word layout: ")
    amount = int(input("Enter the amount of generated values: "))

    for i in range(amount):
        for c in layout:
            if (c == 'C'):
                print(id_generator(consonants), end='')
            elif (c == 'V'):
                print(id_generator(vowels), end='')
            elif (c == 'X'):
                print(id_generator(), end='')
            else:
                print(c, end='')
        print()

if __name__=='__main__':
    main()