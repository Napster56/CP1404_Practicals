"""CP1404 Practical07 - Client code to use the ProgrammingLanguage class."""

from Prac07.programminglanguage import ProgrammingLanguage
from operator import itemgetter


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    program_languages = [ruby, python, vb]

    # print(python)

    dynamic_list = [item for item in program_languages if item.is_dynamic() is True]
    print("The dynamically typed languages are: ")

    for item in dynamic_list:
        print(item)  # TODO how to print only the name of item

main()
