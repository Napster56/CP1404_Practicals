"""
Program gets two numbers as user input;
then asks the user ro select from the menu below:
 1. Show the even numbers from x to y
 2. Show the odd numbers from x to y
 3. Show the squares from x to y
 4. Exit the program
"""


def get_num(prompt):
    num = int(input(prompt))
    return num


def menu():
    print("Please choose from the following: \n (1.) Show the even numbers from x to y \
    \n (2.) Show the odd numbers from x to y \n (3.) Show the squares from x to y \
    \n (4.) Exit the program")
    choice = int(input("Enter your choice: "))
    return choice


def main():
    num1 = get_num("Enter the first number of the sequence.")
    num2 = get_num("Enter the second number of the sequence.")
    choice = menu()
    for i in range(num1, num2 + 1):
        if choice == 1 and i % 2 == 0:
            print(i, end=" ")
        elif choice == 2 and i % 2 == 1:
            print(i, end=" ")
        elif choice == 3:
            i = i * i
            print(i, end=" ")
    if choice == 4:
        print("Goodbye.")
main()