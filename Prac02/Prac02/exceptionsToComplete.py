"""
CP1404/CP5632 - Practical
Program gets an integer from the user, but will not crash if user does not enter an integer.
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an integer: "))
        finished = True
    except (TypeError, ValueError):
        print("Please enter a valid integer.")
print("Valid result is:", result)
