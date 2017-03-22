"""
Program asks the user for their name and then prints name based on how many
characters user wants to skip.
"""


def get_name2():
    name = input("Enter your name: ")
    name = name.replace(" ", "")
    while name == "":
        print("Name cannot be blank.")
        name = input("Enter your name: ")
    return name


def main():
    name = get_name2()
    num = int(input("Enter the number of letters to skip over?"))
    odd_name = name[:: num]
    print("Your name is: {}".format(odd_name))

main()
