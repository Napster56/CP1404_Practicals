"""
Program to print a word n times.
"""

word = input("Enter the word: ")
times = int(input("How many times to repeat: "))


def print_recursively(word, times):
    if times == 1:
        return [word]
    else:
        return [word] + print_recursively(times - 1, word)

print(print_recursively(word, times))
