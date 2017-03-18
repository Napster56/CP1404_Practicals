"""
Tyrone Napoli
"""

user_name = input("Enter your name: ")
while user_name == "":
    print("Invalid input.")
    user_name = input("Enter your name: ")
new_name = ""
for character in range(len(user_name), 2):
    new_name += character
    print(new_name)