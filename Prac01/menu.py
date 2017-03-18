"""
Program asks for the user's name and offers three menu choices as below:
- 'Hello'
- 'Goodbye'
- 'Quit'
if the user enters an invalid choice an error message is
displayed and then asks again for the user's choice.
"""

def menu():
    print("Please choose from the following: \n (H)ello \n (G)oodbye \n (Q)uit")

def main():
    user_name = input("Enter your name: ")
    menu()
    choice = input().upper()
    while choice != "Q":
        if choice == "H":
            print("Hello", user_name)
            choice = input().upper()
        elif choice == "G":
            print("Goodbye", user_name)
            choice = input().upper()
        else:
            print("Invalid choice.")
            menu()
            choice = input("Enter your choice.").upper()
    print("Goodbye.")
main()