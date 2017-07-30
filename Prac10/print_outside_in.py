"""
Write a program that prints a string from the outside in, using recursion.
"""


text = input("Enter a string: ")

def print_ouside_in(text):
    if len(text) <= 1:
        return text
    else:
        return (text[0] + text[-1]) + print_ouside_in(text[1:-1])


print(print_ouside_in(text))
