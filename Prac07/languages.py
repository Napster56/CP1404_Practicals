"""CP1404 Practical07 - Client code to use the ProgrammingLanguage class."""

from Prac07.programminglanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    program_languages = [ruby, python, vb]

    # print(python)
    dynamic_languages = []
    print("The dynamically typed languages are: ")
    for item in program_languages:
        if item.is_dynamic() is True:
            dynamic_languages.append(item)
    for item, value in enumerate(dynamic_languages):
        print(value[0])
            # print(program_languages)

    # [item for item in program_languages if is_dynamic(self) == True]

main()
